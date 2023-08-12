/**
 * @fileoverview Main CLI object.
 * @author Nicholas C. Zakas
 */

"use strict";

/*
 * The CLI object should *not* call process.exit() directly. It should only return
 * exit codes. This allows other programs to use the CLI object and still control
 * when the program exits.
 */

//------------------------------------------------------------------------------
// Requirements
//------------------------------------------------------------------------------

const fs = require("fs"),
    path = require("path"),
    rules = require("./rules"),
    eslint = require("./eslint"),
    defaultOptions = require("../conf/cli-options"),
    IgnoredPaths = require("./ignored-paths"),
    Config = require("./config"),
    Plugins = require("./config/plugins"),
    fileEntryCache = require("file-entry-cache"),
    globUtil = require("./util/glob-util"),
    SourceCodeFixer = require("./util/source-code-fixer"),
    validator = require("./config/config-validator"),
    stringify = require("json-stable-stringify"),
    hash = require("./util/hash"),

    pkg = require("../package.json");

const debug = require("debug")("eslint:cli-engine");

//------------------------------------------------------------------------------
// Typedefs
//------------------------------------------------------------------------------

/**
 * The options to configure a CLI engine with.
 * @typedef {Object} CLIEngineOptions
 * @property {boolean} allowInlineConfig Enable or disable inline configuration comments.
 * @property {boolean|Object} baseConfig Base config object. True enables recommend rules and environments.
 * @property {boolean} cache Enable result caching.
 * @property {string} cacheLocation The cache file to use instead of .eslintcache.
 * @property {string} configFile The configuration file to use.
 * @property {string} cwd The value to use for the current working directory.
 * @property {string[]} envs An array of environments to load.
 * @property {string[]} extensions An array of file extensions to check.
 * @property {boolean} fix Execute in autofix mode.
 * @property {string[]} globals An array of global variables to declare.
 * @property {boolean} ignore False disables use of .eslintignore.
 * @property {string} ignorePath The ignore file to use instead of .eslintignore.
 * @property {string} ignorePattern A glob pattern of files to ignore.
 * @property {boolean} useEslintrc False disables looking for .eslintrc
 * @property {string} parser The name of the parser to use.
 * @property {Object} parserOptions An object of parserOption settings to use.
 * @property {string[]} plugins An array of plugins to load.
 * @property {Object<string,*>} rules An object of rules to use.
 * @property {string[]} rulePaths An array of directories to load custom rules from.
 */

/**
 * A linting warning or error.
 * @typedef {Object} LintMessage
 * @property {string} message The message to display to the user.
 */

/**
 * A linting result.
 * @typedef {Object} LintResult
 * @property {string} filePath The path to the file that was linted.
 * @property {LintMessage[]} messages All of the messages for the result.
 * @property {number} errorCount Number or errors for the result.
 * @property {number} warningCount Number or warnings for the result.
 * @property {string=} [source] The source code of the fi
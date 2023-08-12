"use strict";

exports.__esModule = true;
exports.File = undefined;

var _typeof2 = require("babel-runtime/helpers/typeof");

var _typeof3 = _interopRequireDefault(_typeof2);

var _getIterator2 = require("babel-runtime/core-js/get-iterator");

var _getIterator3 = _interopRequireDefault(_getIterator2);

var _create = require("babel-runtime/core-js/object/create");

var _create2 = _interopRequireDefault(_create);

var _assign = require("babel-runtime/core-js/object/assign");

var _assign2 = _interopRequireDefault(_assign);

var _classCallCheck2 = require("babel-runtime/helpers/classCallCheck");

var _classCallCheck3 = _interopRequireDefault(_classCallCheck2);

var _possibleConstructorReturn2 = require("babel-runtime/helpers/possibleConstructorReturn");

var _possibleConstructorReturn3 = _interopRequireDefault(_possibleConstructorReturn2);

var _inherits2 = require("babel-runtime/helpers/inherits");

var _inherits3 = _interopRequireDefault(_inherits2);

var _babelHelpers = require("babel-helpers");

var _babelHelpers2 = _interopRequireDefault(_babelHelpers);

var _metadata = require("./metadata");

var metadataVisitor = _interopRequireWildcard(_metadata);

var _convertSourceMap = require("convert-source-map");

var _convertSourceMap2 = _interopRequireDefault(_convertSourceMap);

var _optionManager = require("./options/option-manager");

var _optionManager2 = _interopRequireDefault(_optionManager);

var _pluginPass = require("../plugin-pass");

var _pluginPass2 = _interopRequireDefault(_pluginPass);

var _babelTraverse = require("babel-traverse");

var _babelTraverse2 = _interopRequireDefault(_babelTraverse);

var _sourceMap = require("source-map");

var _sourceMap2 = _interopRequireDefault(_sourceMap);

var _babelGenerator = require("babel-generator");

var _babelGenerator2 = _interopRequireDefault(_babelGenerator);

var _babelCodeFrame = require("babel-code-frame");

var _babelCodeFrame2 = _interopRequireDefault(_babelCodeFrame);

var _defaults = require("lodash/defaults");

var _defaults2 = _interopRequireDefault(_defaults);

var _logger = require("./logger");

var _logger2 = _interopRequireDefault(_logger);

var _store = require("../../store");

var _store2 = _interopRequireDefault(_store);

var _babylon = require("babylon");

var _util = require("../../util");

var util = _interopRequireWildcard(_util);

var _path = require("path");

var _path2 = _interopRequireDefault(_path);

var _babelTypes = require("babel-types");

var t = _interopRequireWildcard(_babelTypes);

var _resolve = require("../../helpers/resolve");

var _resolve2 = _interopRequireDefault(_
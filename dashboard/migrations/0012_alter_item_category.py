# Generated by Django 4.2 on 2023-08-25 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_alter_item_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('other', 'Other')], max_length=10, null=True),
        ),
    ]

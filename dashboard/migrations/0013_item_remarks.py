# Generated by Django 4.2 on 2023-08-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_alter_item_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='remarks',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
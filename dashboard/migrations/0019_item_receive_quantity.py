# Generated by Django 4.2 on 2023-08-31 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_item_last_updated_alter_item_registered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='receive_quantity',
            field=models.PositiveIntegerField(blank=True, default='0', null=True),
        ),
    ]
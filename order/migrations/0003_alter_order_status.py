# Generated by Django 4.2 on 2023-08-22 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_order_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default='Pending', max_length=10, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razv4_0', '0013_customer_deleted_driver_deleted_razvozka_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivericons',
            name='icon_url',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-11 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razv4_0', '0022_driver_car_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='car_type',
            field=models.CharField(max_length=40, null=True),
        ),
    ]

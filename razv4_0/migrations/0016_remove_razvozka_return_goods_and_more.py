# Generated by Django 4.2.3 on 2023-08-04 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('razv4_0', '0015_razvozka_returns_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='razvozka',
            name='return_goods',
        ),
        migrations.AddField(
            model_name='razvozka',
            name='return_close_without_delivery',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

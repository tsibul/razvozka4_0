# Generated by Django 4.2.3 on 2023-07-24 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('razv4_0', '0004_alter_razvozka_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=2)),
                ('description', models.CharField(max_length=100)),
                ('phone1', models.CharField(max_length=11)),
                ('phone2', models.CharField(blank=True, max_length=11, null=True)),
                ('car_no', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='razvozka',
            name='date_create',
            field=models.DateField(help_text='date of create razvozka', null=True),
        ),
        migrations.AlterField(
            model_name='razvozka',
            name='date_until',
            field=models.DateField(help_text='plan (last) date of transportation', null=True),
        ),
        migrations.AlterField(
            model_name='razvozka',
            name='fulfilled',
            field=models.BooleanField(default=False, help_text='True is fulfilled'),
        ),
        migrations.AddField(
            model_name='razvozka',
            name='driver.py',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='razv4_0.driver.py'),
        ),
    ]

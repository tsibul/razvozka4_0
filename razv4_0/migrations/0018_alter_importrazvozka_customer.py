# Generated by Django 4.2.3 on 2023-08-05 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('razv4_0', '0017_importcustomer_importrazvozka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importrazvozka',
            name='customer',
            field=models.ForeignKey(blank=True, help_text='customer base if exist', null=True, on_delete=django.db.models.deletion.SET_NULL, to='razv4_0.importcustomer'),
        ),
    ]

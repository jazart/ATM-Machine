# Generated by Django 2.1.3 on 2018-12-03 16:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0003_auto_20181202_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atm',
            name='num',
        ),
        migrations.RemoveField(
            model_name='atm',
            name='refillDate',
        ),
        migrations.AddField(
            model_name='atm',
            name='Lrefill',
            field=models.DateField(default=datetime.datetime(2018, 12, 3, 11, 51, 2, 254602)),
        ),
        migrations.AddField(
            model_name='atm',
            name='Minbalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='atm',
            name='NrefillDate',
            field=models.DateField(default=datetime.datetime(2018, 12, 3, 11, 51, 2, 255602)),
        ),
    ]
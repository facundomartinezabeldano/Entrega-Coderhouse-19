# Generated by Django 4.0.4 on 2022-05-27 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tp_entrega_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relative',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='relative',
            name='birth_date',
            field=models.DateField(default=datetime.date(2022, 5, 27)),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-21 07:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0020_legend_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='time',
            field=models.TimeField(default=datetime.time, verbose_name=datetime.time),
        ),
        migrations.AlterField(
            model_name='legend',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]

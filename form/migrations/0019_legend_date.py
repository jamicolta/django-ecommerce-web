# Generated by Django 4.1.3 on 2022-12-21 06:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0018_legend'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name=datetime.date.today),
        ),
    ]

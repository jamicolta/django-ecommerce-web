# Generated by Django 4.1.3 on 2022-12-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0021_legend_time_alter_legend_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legend',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
    ]
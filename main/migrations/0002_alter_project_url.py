# Generated by Django 4.1.3 on 2022-11-14 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0019_legend_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='legend',
            name='user',
            field=models.CharField(default='Usuario público', max_length=50),
        ),
    ]

# Generated by Django 4.1.3 on 2022-12-14 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0013_remove_form_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='image',
            field=models.ImageField(upload_to='main/images/'),
        ),
    ]

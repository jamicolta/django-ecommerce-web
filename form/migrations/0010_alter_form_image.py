# Generated by Django 4.1.3 on 2022-12-13 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_alter_form_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='image',
            field=models.ImageField(default='main/images/briefcase.jpg', upload_to='main/images'),
        ),
    ]
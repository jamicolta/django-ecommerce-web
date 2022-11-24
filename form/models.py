from django.db import models
import datetime

# Create your models here.
class Form(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=100)
    description = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ipsam, ex.')
    image = models.ImageField(upload_to='main/images', default='main/images/briefcase.jpg')
    date = models.DateField(datetime.date.today, default=datetime.date.today)
    rol = models.CharField(max_length=50, default='Usuario público')
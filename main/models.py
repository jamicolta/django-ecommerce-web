from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='main/images/')
    date = models.DateField(datetime.date.today)
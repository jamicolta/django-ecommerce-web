from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='main/images/')
    price = models.FloatField()
from django.db import models
import datetime

# Create your models here.
class Form(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa omnis eveniet illum commodi officiis nulla soluta similique aliquid pariatur obcaecati iste autem quo nihil eius error assumenda porro, magnam fugiat nobis numquam. Repellendus nisi accusamus harum dolorum totam ipsum error.",
    )
    description = models.TextField()
    image = models.ImageField(upload_to="form/images")
    date = models.DateField(datetime.date.today, default=datetime.date.today)
    rol = models.CharField(max_length=50, default="Usuario público")


class Legend(models.Model):
    user = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField(datetime.date.today, default=datetime.date.today)
    time = models.TimeField(auto_now=True)

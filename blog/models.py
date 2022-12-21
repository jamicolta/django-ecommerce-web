from django.db import models
import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(
        max_length=500,
        default="Lorem ipsum dolor sit amet consectetur adipisicing elit. Culpa omnis eveniet illum commodi officiis nulla soluta similique aliquid pariatur obcaecati iste autem quo nihil eius error assumenda porro, magnam fugiat nobis numquam. Repellendus nisi accusamus harum dolorum totam ipsum error.",
    )
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)
    rol = models.CharField(max_length=50, default="Administrador")

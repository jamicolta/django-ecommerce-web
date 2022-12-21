from django.db import models
import datetime

# Create your models here.
class Form(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=100, default='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Provident enim voluptatibus porro doloribus deserunt laudantium beatae dicta distinctio sunt amet assumenda quos perspiciatis harum animi consequatur, odio nihil et reprehenderit totam eaque consequuntur temporibus voluptate optio. Quos provident, cumque quia aut esse sequi unde excepturi dolor tenetur sint hic magni voluptate dolore dolorem, voluptas quasi quo quam. Aliquam corporis neque error quisquam iure labore. Quae, nesciunt fugit, totam corporis iusto vero soluta autem eos esse magni molestiae ab aperiam ducimus repellat voluptas delectus.')
    description = models.TextField()
    image = models.ImageField(upload_to='form/images')
    date = models.DateField(datetime.date.today, default=datetime.date.today)
    rol = models.CharField(max_length=50, default='Usuario público')
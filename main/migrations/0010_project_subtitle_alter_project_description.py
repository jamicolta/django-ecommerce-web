# Generated by Django 4.1.3 on 2022-12-21 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_delete_nextmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='subtitle',
            field=models.CharField(default='Lorem, ipsum dolor sit amet consectetur adipisicing elit. Provident enim voluptatibus porro doloribus deserunt laudantium beatae dicta distinctio sunt amet assumenda quos perspiciatis harum animi consequatur, odio nihil et reprehenderit totam eaque consequuntur temporibus voluptate optio. Quos provident, cumque quia aut esse sequi unde excepturi dolor tenetur sint hic magni voluptate dolore dolorem, voluptas quasi quo quam. Aliquam corporis neque error quisquam iure labore. Quae, nesciunt fugit, totam corporis iusto vero soluta autem eos esse magni molestiae ab aperiam ducimus repellat voluptas delectus.', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]

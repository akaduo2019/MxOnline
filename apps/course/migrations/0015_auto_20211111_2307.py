# Generated by Django 2.0.2 on 2021-11-11 23:07

import course.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_auto_20211111_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.FileField(upload_to=course.models.CourseResource.get_photo_path, verbose_name='资源文件'),
        ),
    ]

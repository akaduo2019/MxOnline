# Generated by Django 2.0.2 on 2021-11-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0010_auto_20180331_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.ImageField(upload_to='course/resource/%Y/%m', verbose_name='资源文件'),
        ),
    ]

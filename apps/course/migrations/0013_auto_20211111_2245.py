# Generated by Django 2.0.2 on 2021-11-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20211111_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseresource',
            name='download',
            field=models.FileField(upload_to='course/resource<django.db.models.fields.related.ForeignKey>', verbose_name='资源文件'),
        ),
    ]

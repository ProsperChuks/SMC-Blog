# Generated by Django 3.2.18 on 2023-04-11 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20230409_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_slide',
            field=models.ManyToManyField(blank=True, to='backend.imageShow'),
        ),
    ]

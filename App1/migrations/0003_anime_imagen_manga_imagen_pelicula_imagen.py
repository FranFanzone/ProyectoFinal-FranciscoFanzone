# Generated by Django 4.1.5 on 2023-02-22 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_avatarimagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='animes'),
        ),
        migrations.AddField(
            model_name='manga',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='mangas'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='peliculas'),
        ),
    ]

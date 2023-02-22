# Generated by Django 4.1.5 on 2023-02-22 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_anime_imagen_manga_imagen_pelicula_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
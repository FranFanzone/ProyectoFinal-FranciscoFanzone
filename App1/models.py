from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):

    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    estudio = models.CharField(max_length=40)
    año = models.DateField()
    capitulos = models.IntegerField(default=0)
    estado = models.CharField(max_length=40)

class Manga(models.Model):

    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    año = models.DateField()
    numeros = models.IntegerField(default=0)
    estado = models.CharField(max_length=40)
    

class Pelicula(models.Model):

    nombre = models.CharField(max_length=40)
    autor = models.CharField(max_length=40)
    director = models.CharField(max_length=40)
    año = models.DateField()
    vistas = models.IntegerField(default=0)
    imdb = models.FloatField(default=0)

class AvatarImagen(models.Model):

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)
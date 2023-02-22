from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from App1.models import *

class AnimeFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    estudio = forms.CharField()
    año = forms.DateField()
    capitulos = forms.IntegerField()
    estado = forms.CharField()
    imagen = forms.ImageField()

class MangaFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    año = forms.DateField()
    numeros = forms.IntegerField()
    estado = forms.CharField()
    imagen = forms.ImageField()

class PeliculaFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    director = forms.CharField()
    año = forms.DateField()
    vistas = forms.IntegerField()
    imdb = forms.FloatField()
    imagen = forms.ImageField()

class RegistroFormulario(UserCreationForm):

    first_name = forms.CharField(label='Nombre:')
    last_name = forms.CharField(label='Apellido:')
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña:', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class EditarUsuarioFormulario(UserCreationForm):

    first_name = forms.CharField(label='Nombre:')
    last_name = forms.CharField(label='Apellido:')
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña:', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1']

class AvatarImagenFormulario(forms.ModelForm):

    class Meta:

        model = AvatarImagen
        fields = ['usuario', 'imagen']




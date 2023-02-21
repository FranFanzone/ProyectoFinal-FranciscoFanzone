from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AnimeFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    estudio = forms.CharField()
    año = forms.DateField()
    capitulos = forms.IntegerField()
    estado = forms.CharField()

class MangaFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    año = forms.DateField()
    numeros = forms.IntegerField()
    estado = forms.CharField()
     

class PeliculaFormulario(forms.Form):

    nombre = forms.CharField()
    autor = forms.CharField()
    director = forms.CharField()
    año = forms.DateField()
    vistas = forms.IntegerField()
    imdb = forms.FloatField()

class RegistroFormulario(UserCreationForm):

    first_name = forms.CharField(label='Nombre:')
    last_name = forms.CharField(label='Apellido:')
    email = forms.EmailField(label='Email:')
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña:', widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


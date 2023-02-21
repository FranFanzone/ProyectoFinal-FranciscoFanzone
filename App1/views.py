from django.shortcuts import render
from App1.models import *
from App1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
def inicio(request):

    return render(request, 'App1/inicio.html')

def registro(request):

    if request.method == 'POST':

        miFormulario = RegistroFormulario(request.POST)

        if miFormulario.is_valid():
            miFormulario.save()

            return render(request, 'App1/inicio.html')
    else:
        miFormulario = RegistroFormulario()

    return render(request, 'App1/autenticacion/registro.html', {'miFormulario':miFormulario})

def iniciar_sesion(request):

    if request.method == 'POST':

        miFormulario = AuthenticationForm(request, data = request.POST)

        if miFormulario.is_valid():

            usuario = miFormulario.cleaned_data.get('username')
            contra = miFormulario.cleaned_data.get('password')

            miUsuario = authenticate(username=usuario, password=contra)

            if miUsuario:

                login(request, miUsuario)
                mensaje = f'{miUsuario}!'

                return render(request, 'App1/inicio.html', {'mensaje':mensaje})
        else:
            mensaje = f'Error, ingresaste mal los datos!'
            
            return render(request, 'App1/inicio.html', {'mensaje':mensaje})
    else:
         
        miFormulario = AuthenticationForm()

    return render(request, 'App1/autenticacion/login.html', {'formulario1':miFormulario})
        
        
    
class ListaAnime(ListView):

    model = Anime

class DetalleAnime(DetailView):

    model = Anime

class CrearAnime(LoginRequiredMixin, CreateView):

    model = Anime
    success_url = '/App1/anime/list/'
    fields = ['nombre','autor','estudio','año','capitulos','estado']

class ActualizarAnime(LoginRequiredMixin, UpdateView):

    model = Anime
    success_url = '/App1/anime/list'
    fields = ['nombre','autor','estudio','año','capitulos','estado']

class BorrarAnime(LoginRequiredMixin, DeleteView):

    model = Anime
    success_url = '/App1/anime/list'
    

class ListaManga(ListView):

    model = Manga

class DetalleManga(DetailView):

    model = Manga

class CrearManga(LoginRequiredMixin, CreateView):

    model = Manga
    success_url = '/App1/manga/list/'
    fields = ['nombre','autor','año','numeros','estado']

class ActualizarManga(LoginRequiredMixin, UpdateView):

    model = Manga
    success_url = '/App1/manga/list'
    fields = ['nombre','autor','año','numeros','estado']

class BorrarManga(LoginRequiredMixin, DeleteView):

    model = Manga
    success_url = '/App1/manga/list'

class ListaPelicula(ListView):

    model = Pelicula

class DetallePelicula(DetailView):

    model = Pelicula

class CrearPelicula(LoginRequiredMixin, CreateView):

    model = Pelicula
    success_url = '/App1/pelicula/list/'
    fields = ['nombre','autor','director','año','vistas', 'imdb']

class ActualizarPelicula(LoginRequiredMixin, UpdateView):

    model = Pelicula
    success_url = '/App1/pelicula/list'
    fields = ['nombre','autor','director','año','vistas', 'imdb']

class BorrarPelicula(LoginRequiredMixin, DeleteView):

    model = Pelicula
    success_url = '/App1/pelicula/list'


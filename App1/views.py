from django.shortcuts import render
from App1.models import *
from App1.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):

    return render(request, 'App1/inicio.html')

#Barra de busqueda

def buscarAnime(request):

    return render(request, 'App1/buscarAnime.html')

def resultadoBusquedaAnime(request):

    if request.method == 'GET':

        nombreBusqueda = request.GET['nombre']
        animeResultado = Anime.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, 'App1/resultadoBusquedaAnime.html', {'nombre':nombreBusqueda, 'resultado':animeResultado})

    return render(request, 'App1/resultadoBusquedaAnime.html')

def buscarManga(request):

    return render(request, 'App1/buscarManga.html')

def resultadoBusquedaManga(request):

    if request.method == 'GET':

        nombreBusqueda = request.GET['nombre']
        mangaResultado = Manga.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, 'App1/resultadoBusquedaManga.html', {'nombre':nombreBusqueda, 'resultado':mangaResultado})

    return render(request, 'App1/resultadoBusquedaManga.html')

def buscarPelicula(request):

    return render(request, 'App1/buscarPelicula.html')

def resultadoBusquedaPelicula(request):

    if request.method == 'GET':

        nombreBusqueda = request.GET['nombre']
        peliculaResultado = Pelicula.objects.filter(nombre__icontains=nombreBusqueda)

        return render(request, 'App1/resultadoBusquedaPelicula.html', {'nombre':nombreBusqueda, 'resultado':peliculaResultado})

    return render(request, 'App1/resultadoBusquedaPelicula.html')

#Crear usuario

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
        
@login_required
def subirImagenAvatar(request):

    if request.method == 'POST':

        miFormulario = AvatarImagenFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = AvatarImagen(usuario=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, 'App1/inicio.html')
    else:
        miFormulario = AvatarImagenFormulario()

    return render(request, 'App1/agregarAvatar.html', {'form':miFormulario})

@login_required
def editarUsuario(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = EditarUsuarioFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']
            usuario.set_password(info['password1'])
            usuario.email = info['email']

            usuario.save()

            return render(request, 'App1/Inicio.html')
    else:
        miFormulario = EditarUsuarioFormulario(initial={'first_name':usuario.first_name, 'last_name':usuario.last_name, 'email':usuario.email,})
    
    return render(request, 'App1/editarUsuario.html', {'form':miFormulario, 'user':usuario})

#acerca de mi

def acercaDeMi(request):

    return render(request, 'App1/acercaDeMi.html')

#vistas Anime, Pelis y Manga   
class ListaAnime(ListView):

    model = Anime

class DetalleAnime(DetailView):

    model = Anime

class CrearAnime(LoginRequiredMixin, CreateView):

    model = Anime
    success_url = '/App1/anime/list/'
    fields = ['nombre','autor','estudio','año','capitulos','estado','imagen']

class ActualizarAnime(LoginRequiredMixin, UpdateView):

    model = Anime
    success_url = '/App1/anime/list'
    fields = ['nombre','autor','estudio','año','capitulos','estado', 'imagen']

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
    fields = ['nombre','autor','año','numeros','estado', 'imagen']

class ActualizarManga(LoginRequiredMixin, UpdateView):

    model = Manga
    success_url = '/App1/manga/list'
    fields = ['nombre','autor','año','numeros','estado', 'imagen']

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
    fields = ['nombre','autor','director','año','vistas', 'imdb', 'imagen']

class ActualizarPelicula(LoginRequiredMixin, UpdateView):

    model = Pelicula
    success_url = '/App1/pelicula/list'
    fields = ['nombre','autor','director','año','vistas', 'imdb', 'imagen']

class BorrarPelicula(LoginRequiredMixin, DeleteView):

    model = Pelicula
    success_url = '/App1/pelicula/list'

#evitar pantalla de errores
def error_404(request, exception):
    return render(request,'App1/error_404.html')


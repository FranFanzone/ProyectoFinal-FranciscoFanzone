from django.urls import path
from App1.views import *
from django.contrib.auth.views import LogoutView
from App1 import views



urlpatterns = [
    path('', inicio, name='inicio'),
    #sector anime
    path('anime/list/', ListaAnime.as_view(), name='ListaAnime'),
    path('anime/<int:pk>', DetalleAnime.as_view(), name='DetalleAnime'),
    path('anime/crear/', CrearAnime.as_view(), name='CrearAnime'),
    path('anime/actualizar/<int:pk>', ActualizarAnime.as_view(), name='ActualizarAnime'),
    path('anime/Borrar/<int:pk>', BorrarAnime.as_view(), name='BorrarAnime'),
    #sector manga
    path('manga/list/', ListaManga.as_view(), name='ListaManga'),
    path('manga/<int:pk>', DetalleManga.as_view(), name='DetalleManga'),
    path('manga/crear/', CrearManga.as_view(), name='CrearManga'),
    path('manga/actualizar/<int:pk>', ActualizarManga.as_view(), name='ActualizarManga'),
    path('manga/Borrar/<int:pk>', BorrarManga.as_view(), name='BorrarManga'),
    #sector peliculas
    path('pelicula/list/', ListaPelicula.as_view(), name='ListaPelicula'),
    path('pelicula/<int:pk>', DetallePelicula.as_view(), name='DetallePelicula'),
    path('pelicula/crear/', CrearPelicula.as_view(), name='CrearPelicula'),
    path('pelicula/actualizar/<int:pk>', ActualizarPelicula.as_view(), name='ActualizarPelicula'),
    path('pelicula/Borrar/<int:pk>', BorrarPelicula.as_view(), name='BorrarPelicula'),
    #sector registro
    path('registro/', registro, name='registro'),
    path('login/', iniciar_sesion, name='login'),
    path('logout/', LogoutView.as_view(template_name='App1/autenticacion/logout.html'), name='logout'),
    path('editarUsuario/', editarUsuario, name='editarUsuario'),
    #sector imagenes
    path('SubirAvatar/', views.subirImagenAvatar, name='AgregarAvatar'),
    #sector buscador
    path('buscarAnime/', buscarAnime, name='buscarAnime'),
    path('resultadoBusquedaAnime/', resultadoBusquedaAnime, name='resultadoBusquedaAnime'),
    
    path('buscarManga/', buscarManga, name='buscarManga'),
    path('resultadoBusquedaManga/', resultadoBusquedaManga, name='resultadoBusquedaManga'),

    path('buscarPelicula/', buscarPelicula, name='buscarPelicula'),
    path('resultadoBusquedaPelicula/', resultadoBusquedaPelicula, name='resultadoBusquedaPelicula'),
    #acerca de mi
    path('acerca/', acercaDeMi, name='acerca'),
]


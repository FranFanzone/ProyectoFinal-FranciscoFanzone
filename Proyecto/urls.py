from django.contrib import admin
from django.urls import path, include
from App1.views import inicio
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('', inicio),
]

handler404 = 'App1.views.error_404'

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
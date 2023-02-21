from django.contrib import admin
from django.urls import path, include
from App1.views import inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('App1/', include('App1.urls')),
    path('', inicio),
]

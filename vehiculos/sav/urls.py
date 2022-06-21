"""sav URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.contrib.auth
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from webapp.views import inicio
from vehiculos.views import registro_vehiculos, ver_detalle, editar_vehiculo, vehiculos_buscados
from usuarios.views import login_user

#Here the links are linked with a function that respond a request
urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio', inicio),
    path('registro_vehiculos', registro_vehiculos, name='registro'),
    path('ver_detalle/<int:id>', ver_detalle),
    path('editar_vehiculo/<int:id>', editar_vehiculo),
    path('vehiculos_buscados', vehiculos_buscados, name='vehiculos_buscados'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
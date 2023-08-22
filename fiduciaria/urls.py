"""fiduciaria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from fiduciaria.views import paginainicio, quienes_somos, obras_en_curso, nuevos_proyectos, contacto, galeria_de_fotos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('paginainicio/', paginainicio, name='paginainicio'),
    path('quienes_somos/', quienes_somos, name='quienes_somos'),
    path('obras_en_curso/', obras_en_curso, name='obras_en_curso'),
    path('nuevos_proyectos/', nuevos_proyectos, name='nuevos_proyectos'),
    path('contacto/', contacto, name='contacto'),
    path('galeria_de_fotos/', galeria_de_fotos, name='galeria_de_fotos'),
]

    
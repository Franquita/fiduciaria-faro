from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

def paginainicio(request):

    return render(request, "base1.html")

def galeria_de_fotos(request):
    return render(request, "galeriafotos.html")

def quienes_somos(request):
    return render(request, "quienessomos.html")

def obras_en_curso(request):
    return render(request, "obrasencurso.html")

def nuevos_proyectos(request):
    return render(request, "nuevosproyectos.html")

def contacto(request):
    return render(request, "contacto.html")





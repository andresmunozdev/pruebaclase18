from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):

    nombre_curso="Python23"
    comision_curso=513254

    curso=Curso(nombre=nombre_curso,comision=comision_curso)
    curso.save()
    respuesta =f"Curso Creado --- {nombre_curso} - {comision_curso}"
    return HttpResponse(respuesta)


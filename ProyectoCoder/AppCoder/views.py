from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(self):

    curso=Curso(nombre = 'Django', camada = '9393939')
    curso.save()
    doc = f"Curso {curso.nombre} camada {curso.camada}"

    return HttpResponse(doc)

def inicio(request):

    return render(request, "AppCoder/inicio.html")

def cursos(request):

    return render(request, "AppCoder/cursos.html")

def profesores(request):

    return render(request, "AppCoder/profesores.html")

def estudiantes(request):

    return render(request, "AppCoder/estudiantes.html")

def entregables(request):

    return render(request, "AppCoder/entregables.html")
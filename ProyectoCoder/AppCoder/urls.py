from django.urls import path
from .views import *


urlpatterns = [
    path ('', inicio),
    path ('cursos/', cursos),
    path ('entregables/', entregables),
    path ('profesores/', profesores),
    path ('estudiantes/', estudiantes),
]
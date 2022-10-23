from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Context, Template, loader
from django.shortcuts import render
from AppFamiliares.models import Familiares

# Create your views here.
def home (request):
    return HttpResponse("""
    <h1> Familiares de Juliana Blanc </h1>
    <br>
    <br>
    """)


def save_familiares(request, parentesco, nombre, edad):
    familiar = Familiares(parentesco=parentesco, nombre=nombre, edad=edad)
    familiar.save()
    # return render(request, 'template1.html', {'Parentesco': parentesco, 'Nombre': nombre, 'Edad': edad} )
    return render(request, 'template1.html', {'nuevo_familiar': familiar} )

def get_familiares (request):
    lista = Familiares.objects.all()
    return render(request, 'lista_familiares.html', {"listado_de_familiares": lista})

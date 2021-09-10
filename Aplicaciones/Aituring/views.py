from django.shortcuts import render, redirect
from .models import Modelo
from django.contrib import messages

# Create your views here.


def home(request):
    ModelosListados = Modelo.objects.all()
    messages.success(request, '¡Modelos listados!')
    return render(request, "gestionModelos.html", {"Modelos": ModelosListados})


def registrarModelo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    Modelo = Modelo.objects.create(
        codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, '¡Modelo registrado!')
    return redirect('/')


def edicionModelo(request, codigo):
    Modelo = Modelo.objects.get(codigo=codigo)
    return render(request, "edicionModelo.html", {"Modelo": Modelo})


def editarModelo(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    Modelo = Modelo.objects.get(codigo=codigo)
    Modelo.nombre = nombre
    Modelo.creditos = creditos
    Modelo.save()

    messages.success(request, '¡Modelo actualizado!')

    return redirect('/')


def eliminarModelo(request, codigo):
    Modelo = Modelo.objects.get(codigo=codigo)
    Modelo.delete()

    messages.success(request, '¡Modelo eliminado!')

    return redirect('/')

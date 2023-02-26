import queue

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DeleteView
from django.template.defaulttags import register
from django.urls import reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout


@register.filter()
def persona_ci(ci):
    try:
        persona = Persona.objects.filter(numero_documento=ci).first()
        return persona.nombre
    except:
        return 'Visitante'


def vista(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'home.html')


def cerrar_sesion(request):
    logout(request)
    return redirect('login')


def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print("entra aca?")
        if form.is_valid():
            print("entra aca?")
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro.html', {'form': form})


colaPrioridad = queue.PriorityQueue()


def solicitarTurno(request):
    if request.method == 'POST':
        form = SolicitarTurnoForm(request.POST)
        if form.is_valid():
            servicio = form.cleaned_data['espcialidad']
            servicio_id = Servicio.objects.filter(nombre=servicio).first().id

            form.save()
            return redirect('listarTurnosServicio', servicio_id)
    else:
        form = SolicitarTurnoForm()
        return render(request, 'registro_clientes.html', {'form': form})


def registrarPersona(request):
    if request.method == 'POST':
        form = RegistrarPersonaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
    form = RegistrarPersonaForm()
    return render(request, 'registrar_personas.html', {'form': form})


class MostrarServicios(ListView):
    model = Servicio
    template_name = 'mostrar_servicio.html'


# mostrar turnos por servicio
def mostrarTurnoServicio(request, servicio_id):
    # mostrar todos los objetos de atencion de esa especialidad
    turnos = Atencion.objects.filter(espcialidad=servicio_id)
    # ordenar por prioridad y por horario de atencion
    turnos = turnos.order_by('-prioridad', '-horario_atencion')
    servicio = Servicio.objects.get(id=servicio_id).nombre
    context = {
        'turnos': turnos,
        'servicio': servicio
    }
    return render(request, 'mostrarTurnosServicio.html', context)


def eliminarTurno(request, pk):
    turno = Atencion.objects.get(id=pk)
    servicio_id = turno.espcialidad.id
    turno.delete()
    return redirect('listarTurnosServicio', servicio_id)

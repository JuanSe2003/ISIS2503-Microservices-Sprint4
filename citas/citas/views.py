from .models import Cita
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
from django.conf import settings
import requests
from .tests import CitaForm
import json
from .logic.cita_logic import crear_cita, get_citas, get_cita


def check_medico(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    medicos = r.json()
    for medico in medicos:
        if data["medico"] == medico["id"]:
            return True
    return False
def check_horario(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    horarios = r.json()
    for horario in horarios:
        if data["horario"] == horario["id"]:
            return True
    return False
def check_paciente(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    pacientes = r.json()
    for paciente in pacientes:
        if data["paciente"] == paciente["id"]:
            return True
    return False

def cita_list(request):
    citas = get_citas()
    context = {'citas':citas}
    return render(request, 'citas.html', context)
def cita_create(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            crear_cita(form)
            messages.add_message(request, messages.SUCCESS, 'Successfully created cita')
            return HttpResponseRedirect(reverse('citaCreate'))
        else:
            print(form.errors)
    else:
        form = CitaForm()

    context = {
        'form': form,
    }
    return render(request, 'citaCreate.html', context)

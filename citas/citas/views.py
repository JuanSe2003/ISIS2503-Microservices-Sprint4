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

def CitaList(request):
    queryset = Cita.objects.all()
    cita_list = list(queryset.values('id', 'medico', 'horario', 'paciente'))
    context= {'citas': cita_list}
    return render(request, 'citas.html', context)
def CitaCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        context = {"form": data_json}
        if check_horario(data_json) == True and check_medico(data_json) == True :
            measurement = Cita()
            measurement.id = data_json['id']
            measurement.medico = data_json['medico']
            measurement.horario = data_json['horario']
            measurement.paciente = data_json['paciente']
            measurement.save()
            context = {"form": measurement}
        return render(request, 'citaCreate.html', context)
        
        
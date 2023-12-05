import requests

from django.conf import settings
from .models import Horario
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def HorarioList(request):
    queryset = HorarioList.objects.all()
    context = list(queryset.values('id', 'profesional','date','hora_inicio','hora_fin','disponible'))
    return JsonResponse(context, safe=False)


def check_medico(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    medicos = r.json()
    for medico in medicos:
        if data["medico"] == medico["id"]:
            return True
    return False

def HorarioCreate(request):
    if request.method == 'POST'and check_medico:
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        horario = Horario()
        horario.id = data_json["id"]
        horario.profesional= data_json["profesional"]
        horario.date = data_json["date"]
        horario.hora_inicio= data_json["hora_inicio"]
        horario.hora_fin= data_json["hora_fin"]
        horario.disponible= data_json["disponible"]
        horario.save()
        return HttpResponse("successfully created horario")
    else:
        return HttpResponse("Error creating horario")
    





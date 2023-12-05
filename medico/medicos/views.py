from .models import Medico
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def MedicoList(request):
    queryset = Medico.objects.all()
    context = list(queryset.values('id', 'name','last_name','especialidad','consultorio'))
    return JsonResponse(context, safe=False)

def MedicoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        medico = Medico()
        medico.id = data_json["id"]
        medico.name = data_json["name"]
        medico.last_name = data_json["last_name"]
        medico.especialidad = data_json["especialidad"]
        medico.consultorio = data_json["consultorio"]
        medico.save()
        return HttpResponse("successfully created medico")
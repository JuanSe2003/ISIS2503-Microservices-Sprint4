from .models import Medico
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from .tests import MedicoForm
from .logic.medico_logic import crear_medico, get_medicos, get_medico
import json
 
def medico_list(request):
    medicos = get_medicos()
    context = {'medicos':medicos}
    return render(request, 'medicos.html', context)


def medico_create(request):
    
    if request.method == 'POST':
            form = MedicoForm(request.POST)
            if form.is_valid():
                crear_medico(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created medico')
                return HttpResponseRedirect(reverse('medicoCreate'))
            else:
                print(form.errors)
    else:
            form = MedicoForm()

    context = {
            'form': form,
    }
    return render(request, 'medicoCreate.html', context)


def get_medico(request):
    medico = get_medico()
    context = {'medico':medico}
    return render(request, 'medico_list.html', context)

from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Horario
from .tests import HorarioForm
from .logic.horario_logic import create_horario, get_horarios, get_horario


def horario_list(request):
    horarios = get_horarios()
    context = {'horarios':horarios}
    return render(request, 'horarios.html', context)

def horario_create(request):

        if request.method == 'POST':
            form = HorarioForm(request.POST)
            if form.is_valid():
                create_horario(form)
                messages.add_message(request, messages.SUCCESS, 'Successfully created horario')
                return HttpResponseRedirect(reverse('horarioCreate'))
            else:
                print(form.errors)
        else:
            form = HorarioForm()

        context = {
            'form': form,
        }
        return render(request, 'horarioCreate.html', context)


#¿?
def get_horario(request):
    horario = get_horario()
    context = {'horario':horario}
    return render(request, 'horarios.html', context)
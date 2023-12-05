from django.test import TestCase

from .models import Horario
from django import forms

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = [
            'id',
            'profesional',
            'date',
            'hora_inicio',
            'hora_fin',
            'disponible',
        ]
        labels = {
            'id': 'Id',
            'profesional': 'Profesional',
            'date': 'Date',
            'hora_inicio': 'Hora_inicio',
            'hora_fin': 'Hora_fin',
            'disponible': 'Disponible',
        }
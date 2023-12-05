from django.test import TestCase
from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'id',
            'medico',
            'horario',
            'paciente'
        ]
        labels = {
            'id':'Id',
            'medico': 'Medico',
            'horario':'Horario',
            'paciente': 'Paciente',

        }
from django.db import models
from medicos.medicos.models import Medico

class Horario(models.Model):
    id=models.IntegerField(primary_key=True)
    profesional = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    date = models.DateField(default='2000-01-01')
    hora_inicio = models.IntegerField(default=0)
    hora_fin = models.IntegerField(default=0)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.date} {self.hora_inicio} {self.hora_fin}'
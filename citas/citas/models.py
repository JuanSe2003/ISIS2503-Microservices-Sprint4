from django.db import models
from medicos.medicos.models import Medico
from horarios.horarios.models import Horario

class Cita(models.Model):
    id=models.IntegerField(primary_key=True)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE,default=None)
    horario =models.ForeignKey(Horario, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return {'id':self.id}
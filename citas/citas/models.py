from django.db import models


class Cita(models.Model):
    id=models.IntegerField(primary_key=True)
    medico = models.CharField(max_length=50)
    paciente =  models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    
    def __str__(self):
        return {'id':self.id}
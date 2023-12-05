from django.db import models
    
class Medico(models.Model):
    id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=200,default="General")
    consultorio = models.CharField(max_length=50,default="A00")
    
    def __str__(self):
        return f'{self.name} {self.last_name} {self.especialidad}'
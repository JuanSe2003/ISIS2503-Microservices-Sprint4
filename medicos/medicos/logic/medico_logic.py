from ..models import Medico

def crear_medico(form):
    medico = form.save()
    medico.save()
    return ()

def get_medicos():
    medico=Medico.objects.all()
    return medico

#¿?
def get_medico(var_pk):
    medico=Medico.objects.get(pk=var_pk)
    return medico

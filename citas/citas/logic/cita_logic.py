from ..models import Cita

def crear_cita(form):
    cita = form.save()
    cita.save()
    return ()

def get_citas():
    cita=Cita.objects.all()
    return cita

#¿sobra?
def get_cita(var_pk):
    cita=Cita.objects.get(pk=var_pk)
    return cita


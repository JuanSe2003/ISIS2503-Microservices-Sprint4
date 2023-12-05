from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^medicos/', views.MedicoList, name='medicoList'),
    url(r'^medicocreate/$', csrf_exempt(views.MedicoCreate), name='medicoCreate'),
]
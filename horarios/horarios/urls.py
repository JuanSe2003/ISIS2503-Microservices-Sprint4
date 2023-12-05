from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^horarios/', views.HorarioList, name='horarioList'),
    url(r'^horariocreate/$', csrf_exempt(views.HorarioCreate), name='horarioCreate'),
]
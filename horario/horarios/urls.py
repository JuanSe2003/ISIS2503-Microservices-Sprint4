from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('horarios/', views.HorarioList, name='horarioList'),
    path('horariocreate/', csrf_exempt(views.HorarioCreate), name='horarioCreate'),
]
from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('citas/', views.cita_list, name='citaList'),
    path('citacreate/', csrf_exempt(views.cita_create), name='citaCreate'),
]
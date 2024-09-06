from django.urls import path
from . import views

app_name = 'candidatos'

urlpatterns = [
    path('', views.listar_candidatos, name='listar_candidatos'),
]
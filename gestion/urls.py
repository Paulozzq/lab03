from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
     path('', views.menu, name='menu'),
    path('registrar_propietario/', views.registrar_propietario, name='registrar_propietario'),
    path('registrar_vehiculo/', views.registrar_vehiculo, name='registrar_vehiculo'),
    path('registrar_entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('registrar_salida/<int:registro_id>/', views.registrar_salida, name='registrar_salida'),
    path('listar_propietarios/', views.listar_propietarios, name='listar_propietarios'),
    path('listar_vehiculos/', views.listar_vehiculos, name='listar_vehiculos'),
    path('listar_registros/', views.listar_registros, name='listar_registros'),
]

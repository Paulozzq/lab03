from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detalle,name='detalle'),
    path('<int:question_id>/vote/', views.votar, name='resultado')
]
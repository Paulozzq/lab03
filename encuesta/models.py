from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateField('Fecha de Publicacion')

class Opcion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    opcion_text = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

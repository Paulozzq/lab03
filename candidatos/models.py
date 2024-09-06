from django.db import models

# Create your models here.

class Candidato(models.Model):
    id_candidato = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100)  
    apellido = models.CharField(max_length=100)  
    ciudad = models.CharField(max_length=100)  
    telefono = models.CharField(max_length=15) 
    dni = models.CharField(max_length=8, unique=True) 
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

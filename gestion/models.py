from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    numero_apartamento = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(default='default@example.com') 

    def __str__(self):
        return f'{self.nombre} - Apartamento: {self.numero_apartamento}'

class Vehiculo(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name='vehiculos')
    matricula = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    color = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.matricula} - {self.marca} {self.modelo}'

class Registro(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_hora_entrada = models.DateTimeField(auto_now_add=True)
    fecha_hora_salida = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.vehiculo} - Entrada: {self.fecha_hora_entrada} - Salida: {self.fecha_hora_salida if self.fecha_hora_salida else "No registrada"}'

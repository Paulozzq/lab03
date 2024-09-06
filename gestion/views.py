from django.shortcuts import render, redirect, get_object_or_404
from .models import Propietario, Vehiculo, Registro
from django.utils import timezone

def menu(request):
    return render(request, 'gestion/menu.html')

def registrar_propietario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        numero_apartamento = request.POST.get('numero_apartamento')
        telefono = request.POST.get('telefono', '')
        email = request.POST.get('email')
        Propietario.objects.create(nombre=nombre, numero_apartamento=numero_apartamento, telefono=telefono, email=email)
        return redirect('gestion:listar_propietarios')
    return render(request, 'gestion/registrar_propietario.html')

def registrar_vehiculo(request):
    if request.method == 'POST':
        propietario_id = request.POST.get('propietario_id')
        matricula = request.POST.get('matricula')
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        color = request.POST.get('color')
        propietario = get_object_or_404(Propietario, id=propietario_id)
        Vehiculo.objects.create(propietario=propietario, matricula=matricula, marca=marca, modelo=modelo, color=color)
        return redirect('gestion:listar_vehiculos')
    propietarios = Propietario.objects.all()
    return render(request, 'gestion/registrar_vehiculo.html', {'propietarios': propietarios})

def registrar_entrada(request):
    if request.method == 'POST':
        vehiculo_id = request.POST.get('vehiculo_id')
        vehiculo = get_object_or_404(Vehiculo, id=vehiculo_id)
        Registro.objects.create(vehiculo=vehiculo, fecha_hora_entrada=timezone.now())
        return redirect('gestion:listar_registros')
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/registrar_entrada.html', {'vehiculos': vehiculos})

def registrar_salida(request, registro_id):
    registro = get_object_or_404(Registro, id=registro_id)
    if request.method == 'POST':
        registro.fecha_hora_salida = timezone.now()
        registro.save()
        return redirect('gestion:listar_registros')
    return render(request, 'gestion/registrar_salida.html', {'registro': registro})

def listar_propietarios(request):
    propietarios = Propietario.objects.prefetch_related('vehiculos').all()
    return render(request, 'gestion/propietarios_list.html', {'propietarios': propietarios})

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'gestion/vehiculos_list.html', {'vehiculos': vehiculos})

def listar_registros(request):
    registros = Registro.objects.all()
    return render(request, 'gestion/registros_list.html', {'registros': registros})

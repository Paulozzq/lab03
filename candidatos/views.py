from django.shortcuts import render
from .models import Candidato

def listar_candidatos(request):
    candidatos = Candidato.objects.all()
    context = {
        'candidatos': candidatos
    }
    return render(request, 'candidatos/index.html', context)

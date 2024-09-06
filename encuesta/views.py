from django.shortcuts import render
from .models import Opcion, Question
# Create your views here.

def index(request):
    Lista_preguntas = Question.objects.order_by('-pub_date')
    context = {
        'question_list': Lista_preguntas,
    }
    return render(request, 'encuesta/index.html', context)

def detalle(request, question_id):
    question = Question.objects.get(pk=question_id)
    context = {'question': question}
    return render(request, 'encuesta/detalle.html', context)

def votar(request, question_id):
    question = Question.objects.get(pk=question_id)
    result = question.opcion_set.get(pk=request.POST['opcion'])
    result.votos += 1
    result.save()
    context = {'question': question}
    return render(request, 'encuesta/resultado.html', {'question': question})


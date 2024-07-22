from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.


from datetime import datetime

data = []
horarios = []
def index(request):
    context = {
        'title': 'Home',
        'horas': horarios
    }
    url = 'home/index.html'
    return render(request, url, context=context)

def monitoria(request):
    context = {
        'title': 'Monitoria',
        'data': data,
        }
    url = 'home/monitorias.html'
    return render(request, url, context=context)

def dados(request):
    context = {
        'title': 'Data',
        'data': data,
    }
    url = 'home/data.html'
    return render(request, url, context=context)

def config(request):
    context = {
        'title': 'Configuração',
    }
    url = 'home/config.html'
    return render(request, url, context=context)


def cadastro(request):
    context = {
        'title': 'Cadastro',
    }
    url = 'home/cadastro.html'
    return render(request, url, context=context)
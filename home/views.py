from django.shortcuts import render
from django.shortcuts import get_object_or_404
from home.models import User
# Create your views here.


from datetime import datetime

horarios = []
def index(request):
    from home.models import Horas
    horarios = Horas.objects.all()

    weekday = {}
    data = [
        {"hora": item.time, 'day': item.day.day} 
        for item in horarios
        ]
    for item in data:
        if item['day'] not in weekday.keys():
            weekday[item['day']] = [item['hora']]
            continue
        weekday[item['day']].append(item['hora'])
    del data
    data = [{"dayweek": key, "time_start": str(value[0]), "time_final": str(value[-1])} for key, value in weekday.items()]

    context = {
        'title': 'Home',
        'horarios': data
    }

    url = 'home/index.html'
    return render(request, url, context=context)

def monitoria(request):
    from home.models import Monitorias
    contacts = Monitorias.objects.all()
    data = [
        {'matricula': item.owner.username, 'nome': f"{item.owner.first_name} {item.owner.last_name}", "data": item.date} 
        for item in contacts
    ]
    context = {
        'title': 'Monitoria',
        'data': data,
        }
    url = 'home/monitorias.html'
    return render(request, url, context=context)

def dados(request):
    context = {
        'title': 'Data',
        'data': [],
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
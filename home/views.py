from django.shortcuts import render
from django.shortcuts import get_object_or_404
from home.models import User
from datetime import datetime


horarios = []
def index(request):
    from home.models import Horas, DataUser
    horarios = Horas.objects.all()
    weekday = {}
    data = [{"hora": item.time, 'day': item.day.day} for item in horarios]
    for item in data:
        if item['day'] not in weekday.keys():
            weekday[item['day']] = [item['hora']]
            continue
        weekday[item['day']].append(item['hora'])
    del data
    data = [{"dayweek": key, "time_start": str(value[0]), "time_final": str(value[-1])} for key, value in weekday.items()]

    context = {
        'title': 'Home',
        'horarios': data,
    }

    url = 'home/index.html'
    return render(request, url, context=context)

def monitoria(request):
    from home.models import Monitorias
    contacts = Monitorias.objects.all().order_by('-date')
    data = [
        {'matricula': item.owner.username, 'nome': f"{item.owner.first_name} {item.owner.last_name}", "data": item.date} if item.date >= datetime.date(datetime.now())
        else None
        for item in contacts 
    ]
    context = {
        'title': 'Monitoria',
        'data': [item for item in data if item is not None],
        }
    url = 'home/monitorias.html'
    return render(request, url, context=context)

def dados(request):

    context = {
        'title': 'Estatísticas',
        'data': [],
    }
    url = 'home/data.html'
    return render(request, url, context=context)

def update(request):
    from home.models import DataUser
    context = {
        'title': 'Update',
    }
    url = 'home/update.html'
    return render(request, url, context=context)
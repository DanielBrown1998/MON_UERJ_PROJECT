from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

def days():
    from home.models import Horas
    horarios = Horas.objects.all()
    weekday = {}
    data = [{"hora": item.time, 'day': item.day.day} for item in horarios]
    for item in data:
        if item['day'] not in weekday.keys():
            weekday[item['day']] = [item['hora']]
            continue
        weekday[item['day']].append(item['hora'])
    data = [{"dayweek": key, "time_start": str(value[0]), "time_final": str(value[-1])} for key, value in weekday.items()]
    return data


def index(request):

    context = {
        'title': 'HOME',
        'horarios': days(),
    }

    url = 'home/index.html'
    return render(request, url, context=context)

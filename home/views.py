from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

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
        'title': 'HOME',
        'horarios': data,
    }

    url = 'home/index.html'
    return render(request, url, context=context)

def monitoria(request):
    from home.models import Monitorias
    contacts = Monitorias.objects.all().order_by('-date')

    data = [
        {'matricula': item.owner.username, 'nome': f"{item.owner.first_name} {item.owner.last_name}", "data": item.date} 
        for item in contacts 
    ]
    paginator = Paginator(data, 10)
    page_number = request.GET.get("page")
    data = paginator.get_page(page_number)
    context = {
        'title': 'Monitoria',
        'data': data,
        }
    url = 'home/monitorias.html'
    return render(request, url, context=context)

def search(request):
    from home.models import Monitorias

    num_items = request.GET.get('num_items')
    order_items = request.GET.get('order_items')
    search_value = request.GET.get('q', '').strip()
    if search_value == '' and num_items == '10' and order_items == 'date':
        return redirect('home:monitorias')

    if order_items != 'date' and order_items is not None:

        contacts = Monitorias.objects\
            .filter(
                Q(owner__username__icontains=search_value) | 
                Q(owner__first_name__icontains=search_value) |
                Q(owner__last_name__icontains=search_value)
                )\
            .order_by(f'owner__{order_items}')
    else:
        contacts = Monitorias.objects\
            .filter(
                Q(owner__username__icontains=search_value) | 
                Q(owner__first_name__icontains=search_value) |
                Q(owner__last_name__icontains=search_value)
                )\
            .order_by('-date')


    data = [
        {
            'matricula': item.owner.username, 
            'nome': f"{item.owner.first_name} {item.owner.last_name}", 
            "data": item.date
        }
        for item in contacts 
    ]
    if num_items:
        pagination = Paginator(data, int(num_items))
    else:
        pagination = Paginator(data, 10)
    page_number = request.GET.get("page")
    data = pagination.get_page(page_number)
    
    context = {
        'title': 'Monitoria',
        'data': data,
        'search': search_value,
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

def config(request):
    from home.models import DataUser, Days, Horas, User, Monitorias
    context = {
        'title': 'Configurações',
    }
    url = 'home/config.html'
    return render(request, url, context=context)

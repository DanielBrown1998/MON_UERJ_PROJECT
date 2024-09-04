from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from home.models import DataUser, User, Horas, Days
from django.db.models import Q
from django.contrib.auth.decorators import login_required


@login_required(login_url="home:home")
def update_hours(request):
    day = request.POST.get('daysweek', '').strip()
    time_start = request.POST.get('time_start', '').strip()
    time_end = request.POST.get('time_end', '').strip()
    print(day, time_start, time_end)
    return redirect('home:config')

@login_required(login_url="home:home")
def update_days(request):
    days = request.POST
    print(days)
    return redirect('home:config')

@login_required(login_url="home:home")
def update_monitorias(request):

    usuario = request.POST.get('username', '').strip()
    monitorias_presentes = request.POST.get('monitorias_presentes', '').strip()
    monitorias = DataUser.objects.get(owner__username=usuario)
    if monitorias.monitorias_marcadas >= int(monitorias_presentes):
        monitorias.monitorias_presentes = int(monitorias_presentes)
        #monitorias.save()
    else:
        print('fora do intervalo')
        #envie uma mensagem de erro
    return redirect('home:config')

@login_required(login_url="home:home")
def search_config(request):

    search_value = str(request.GET.get('q', '')).strip()
    if not search_value:
        redirect('home:config')

    data_user = DataUser.objects.filter(
        Q(owner__username__icontains=search_value) |
        Q(owner__first_name__icontains=search_value) |
        Q(owner__first_name__icontains=search_value)
    )
    days = Days.objects.all()
    horas = Horas.objects.all().order_by('day')
    data = [{
        "usuario": user.owner, 
        "monitorias_presentes": user.monitorias_presentes, 
        "monitorias_marcadas": user.monitorias_marcadas} 
        for user in data_user
        ]
    hr = [
        {"time": h.time, "day": h.day.day} 
        for h in horas
        ]
    pagination = Paginator(data, 10)
    page_number = request.GET.get("page")
    data = pagination.get_page(page_number)
    context = {
        'title': f'Configurações-{search_value}',
        'data': data,
        'search': search_value,
        'daysweek': [
            'segunda-feira', 
            'terça-feira', 
            'quarta-feira', 
            'quinta-feira', 
            'sexta-feira'
            ],
        'days': [str(dia).strip() for dia in days],
        'horas': hr,
    }
    url = 'home/config.html'
    return render(request, url, context=context)

@login_required(login_url="home:home")
def config(request):

    data_user = DataUser.objects.all()
    days = Days.objects.all()

    horas = Horas.objects.all().order_by('day')
    data = [{
        "usuario": user.owner, 
        "monitorias_presentes": user.monitorias_presentes, 
        "monitorias_marcadas": user.monitorias_marcadas} 
        for user in data_user
        ]
    hr = [{"time": h.time, "day": h.day.day} for h in horas]

    pagination = Paginator(data, 10)
    page_number = request.GET.get("page")
    data = pagination.get_page(page_number)

    context = {
        'title': 'Configurações',
        'data': data,
        'daysweek': [
            'segunda-feira', 
            'terça-feira', 
            'quarta-feira', 
            'quinta-feira', 
            'sexta-feira'
            ],
        'days': [str(dia).strip() for dia in days],
        'horas': hr,
    }
    
    url = 'home/config.html'
    return render(request, url, context=context)

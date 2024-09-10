from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import Days
from datetime import datetime, timedelta
from django.db.models import Q
from django.core.paginator import Paginator
from home.models import Monitorias
from django.contrib.auth.decorators import login_required
from home.views import message


def monitoria(request):
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

@login_required(login_url='home:home')
def marcar_monitoria(request):
    all_weekdays = [
        'segunda-feira', 
        'terça-feira', 
        'quarta-feira', 
        'quinta-feira', 
        'sexta-feira', 
        'sábado', 
        'domingo'
    ]
    today = datetime.today()
    today_str = datetime.strftime(today, '%Y-%m-%d')
    date = request.POST.get('date')
    if not date:
        message(request, 'Informe uma data')
        return redirect('home:monitorias')
    
    
    date_time = datetime.strptime(date, '%Y-%m-%d')

    if date_time < today:
        message(request, 'Data inválida')
        return redirect('home:monitorias')

    if date_time >= today + timedelta(days=7):
        message(request, 'escolha entre os próximos 7 dias')
        return redirect('home:monitorias')

    weekday = datetime.weekday(date_time)
    weekdays_possible = Days.objects.all()
    
    weekdays_possible = [
        all_weekdays.index(item.day) 
        for item in weekdays_possible 
        if item.day in all_weekdays
        ]

    if weekday not in weekdays_possible:
        message(request, 'Verifique os dias disponíveis da monitoria')
        return redirect('home:monitorias')

    info = request.POST.get('text', '')
    user = request.user

    if Monitorias.objects.filter(Q(date=date) & Q(owner=user)).exists():
        message(request, 'Você já marcou monitoria para este dia')
        return redirect('home:monitorias')
    
    monitoria = Monitorias(date=date, owner=user)
    #monitoria.save()
    message(request, 'Monitoria marcada com sucesso', sucesss=True)
    return redirect('home:monitorias')

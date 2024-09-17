from django.shortcuts import render, redirect
from home.models import Days
from datetime import datetime, timedelta
from django.db.models import Q
from django.core.paginator import Paginator
from home.models import Monitorias, DataUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import get_user
from django.core.mail import send_mail
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

    if date_time > today + timedelta(days=7):
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
    user = get_user(request)

    try:
        monitoria_user = Monitorias.objects.get(Q(date=date) & Q(owner=user))
    except Monitorias.DoesNotExist:
        monitoria_user = None
    
    if monitoria_user:
        message(request, 'Você já marcou monitoria para este dia')
        return redirect('home:monitorias')
    
    try:
        limit_monitoria = Monitorias.objects.filter(date=date)
    except Monitorias.DoesNotExist:
        limit_monitoria = []

    if len(limit_monitoria) == 5:
        message(request, 'Esse dia já atingiu o máximo de monitorias possíveis')
        return redirect('home:monitorias')

    try:
        data_user = DataUser.objects.get(owner = user)
    except DataUser.DoesNotExist:
        data_user = DataUser(owner=user)
        data_user.save()
    data_user.monitorias_marcadas += 1

    Monitorias.objects.create(
        date=date,
        owner=user,
    )
    data_user.save() 
    super_user = User.objects.get(
        is_superuser=True
    )
    
    message(request, 'Monitoria marcada com sucesso', sucesss=True)
    return redirect('home:monitorias')

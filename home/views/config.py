from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from home.models import User
from django.db.models import Q

def config(request):
    from home.models import DataUser, Days, Horas

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
    print(*days, sep="\n")

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

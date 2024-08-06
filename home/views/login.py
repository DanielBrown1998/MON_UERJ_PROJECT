from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import DataUser, User
from django.db.models import Q
from home.models import Matriculas
from home.views import days

def login(request):
    matricula = request.POST.get('matricula').strip()
    matriculas_cadastradas = Matriculas.objects.filter(matricula__icontains = matricula)

    if not matriculas_cadastradas:
        print('não foi possível encontrar sua matrícula')
        return redirect('home:home')
    
    user = User.objects.filter(
        Q(username__icontains = matricula) 
    )

    if not user:
        print('não foi possível encontrar seu usuário')
        return redirect('home:home')

    print('usuário encontrado!')
    context = {
        'title': 'login',
        'horarios': days(),
        'username': matricula,
    }

    url = 'home/login.html'
    return render(request, url, context=context)
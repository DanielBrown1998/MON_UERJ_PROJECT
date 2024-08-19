from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.login import Login
from home.models import DataUser, User
from django.db.models import Q
from home.models import Matriculas
from home.views import days

def login(request):
    
    matricula = str(request.POST.get('matricula', '')).strip()
    
    password = request.POST.get('password', '')

    if password:
        form = Login(
            matricula,
            request.POST
        )
        if form.is_valid():
            #aqui o login será realizado
            return redirect('home:home')
        context = {
            'title': 'login',
            'horarios': days(),
            'form': form,
        }
        url = 'home/login.html'
        return render(request, url, context=context)

    if matricula:
        matriculas_cadastradas = Matriculas.objects.filter(matricula__icontains = matricula)
        
        if not matriculas_cadastradas:
            print('não foi possível encontrar sua matrícula')
            return redirect('home:home')
        user = User.objects.filter(
            Q(username__icontains = matricula) 
        )
        if not user:
            print(
                'não foi possível encontrar seu usuário'
                )
            context = {
                'title': 'Cadastro',
                'username': matricula,
            }
            url = 'home/cadastro.html'
            return render(request, url, context)
    print('usuário encontrado!')
    context = {
        'title': 'login',
        'horarios': days(),
        'username': matricula,
        'form': Login(
            matricula
            )
    }
    url = 'home/login.html'
    return render(request, url, context=context)

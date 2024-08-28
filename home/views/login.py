from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.login import Login
from home.forms.update_create_form import UpdateOrCreateForm
from django.contrib.auth.models import User
from django.db.models import Q
from home.models import Matriculas
from home.views import days

def login(request):
    
    matricula = str(request.POST.get('matricula', '')).strip()
    if len(matricula) != 12:
        return redirect('home:home')
    
    password = request.POST.get('password', '')

    if password:
        form = Login(
            matricula,
            request.POST
        )
        if form.is_valid():
            #aqui o login será realizado
            context = {
            'title': 'Home',
            'horarios': days(),
            'form': form,
            }
            url = 'home/index.html'
            return render(request, url, context=context)
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
            form = UpdateOrCreateForm(
                matricula = matricula
            )
            context = {
                'title': 'Cadastro',
                'form': form
            }
            url = 'home/cadastro.html'
            return render(request, url, context)
    print('usuário encontrado!')
    context = {
        'title': 'login',
        'username': matricula,
        'horarios': days(),
        'form': Login(
            matricula
            )
    }
    url = 'home/login.html'
    return render(request, url, context=context)

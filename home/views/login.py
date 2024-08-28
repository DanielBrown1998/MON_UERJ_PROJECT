from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.login import Login
from home.forms.update_create_form import UpdateOrCreateForm
from django.contrib.auth.models import User
from django.db.models import Q
from home.models import Matriculas
from home.views import days, message

def login(request):
    
    matricula = str(request.POST.get('matricula', '')).strip()
    password = request.POST.get('password', '')

    if password:
        form = Login(
            matricula,
            request.POST
        )
        if form.is_valid():
            message(request, 'Login realizado', sucesss=True)
            #aqui o login será realizado
            context = {
            'title': 'Home',
            'horarios': days(),
            'form': form,
            }
            url = 'home/index.html'
            return render(request, url, context=context)
        
        message(request, 'Login inválido', error=True)
        context = {
            'title': 'login',
            'horarios': days(),
            'form': form,
        }
        url = 'home/login.html'
        return render(request, url, context=context)

    if len(matricula) != 12:
        message(request, 'Matrícula inválida', error=True)
        return redirect('home:home')

    if matricula:
        matriculas_cadastradas = Matriculas.objects.filter(matricula__icontains = matricula)
        
        if not matriculas_cadastradas:
            msg ='não foi possível encontrar sua matrícula'
            message(request, msg, error=True)
            return redirect('home:home')
        user = User.objects.filter(
            Q(username__icontains = matricula) 
        )
        if not user:
            msg = 'não foi possível encontrar seu usuário, cadastre-se!!!'
            message(request, msg)                
            form = UpdateOrCreateForm(
                matricula = matricula
            )
            context = {
                'title': 'Cadastro',
                'form': form
            }
            url = 'home/cadastro.html'
            return render(request, url, context)
    
    msg = 'usuário encontrado!'
    message(request, msg, sucesss=True)
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

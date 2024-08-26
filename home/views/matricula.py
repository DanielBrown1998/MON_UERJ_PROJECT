from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

def matricula(request):
    from home.models import Matriculas
    matriculas = Matriculas.objects.all()
    context = {
        'title': 'Matriculas',
        'matriculas': matriculas,
    }

    url = 'home/matricula.html'
    return render(request, url, context=context)

def create(request):
    context = {
        'title': 'Criando Matricula',
        }
    matricula = request.POST.get('matricula', '').strip()
    if matricula:
        #aqui será realizado o salvamento da matricula na tabela matrícula
        print(matricula)
    return redirect('home:matricula')


def update_matricula(request):
    context = {
        'title': 'atualizando Matricula',
        }
    
    matricula_antiga_id = request.POST.get('matricula_antiga_id', '').strip()
    matricula_nova = request.POST.get('matricula_nova', '').strip()
    if matricula_nova:
        print(matricula_nova)
    if matricula_antiga_id:
        print(matricula_antiga_id)
    return redirect('home:matricula')

def delete_matricula(request):
    title = {
        'title': 'Deletando Matricula',
    }
    matricula = request.POST.get('matricula', '').strip()
    delete_all = request.POST.get('delete_all', '').strip()
    if delete_all:
        print(delete_all)
    if matricula:
        print(matricula)
    return redirect('home:matricula')

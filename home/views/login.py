from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from home.models import DataUser, User
from django.db.models import Q
from home.models import Matriculas

def login(request):
    matricula = request.POST.get('matricula').strip()
    matriculas_cadastradas = Matriculas.objects.filter(matricula__icontains = matricula)
    print(matricula)
    if not matriculas_cadastradas:
        print('não foi possível encontrar sua matrícula')
        return redirect('home:home')

    context = {
        'username': matricula,
    }
    url = 'home/login.html'

    return render(request, url, context=context)
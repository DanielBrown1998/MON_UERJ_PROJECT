from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

def config(request):
    from home.models import DataUser, Days, Horas, Monitorias
    context = {
        'title': 'Configurações',
    }
    url = 'home/config.html'
    return render(request, url, context=context)

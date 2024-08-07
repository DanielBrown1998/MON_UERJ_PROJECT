from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from home.models import User        


def usuarios(request):
    users = User.objects.all().order_by('username')
    pagination = Paginator(users, 10)
    page_number = request.GET.get('page')
    users = pagination.get_page(page_number)
    
    context = {
        'title': 'Usuários',
        'data': users,
    }

    url = 'home/usuarios.html'
    return render(request, url, context=context)

# todo: fazer o search do usuario, assim como o update e delete 
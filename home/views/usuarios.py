from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from home.models import User        

def search_usuarios(request):
    search_value = str(request.GET.get('q', '')).strip()
    if not search_value:
        return redirect('home:usuarios')
    users = User.objects.filter(
        Q(username__icontains=search_value) |
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value)
    )
    pagination = Paginator(users, 10)
    page_number = request.GET.get('page')
    users = pagination.get_page(page_number)
    
    context = {
        'title': 'Usuários',
        'search': search_value,
        'data': users,
    }

    url = 'home/usuarios.html'
    return render(request, url, context=context)


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
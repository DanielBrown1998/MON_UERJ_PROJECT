from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator

def create(request):
    context = {
        'title': 'Create',
    }
    url = 'home/create.html'
    return render(request, url, context=context)

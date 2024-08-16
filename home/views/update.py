from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.updateform import UpdateForm
from home.models import User
from datetime import datetime
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms
from django.core.exceptions import ValidationError


def update(request):
    
    if request.method == 'POST':
        print(request.POST)
        context = {
        'title': 'Update',
        'form': UpdateForm(
            request.POST
            ),
        }
        url = 'home/update.html'
        return render(request, url, context=context)
        





    context = {
        'title': 'Update',
        'form': UpdateForm(),
    }
    url = 'home/update.html'
    return render(request, url, context=context)

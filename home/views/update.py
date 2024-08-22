from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.update_create_form import UpdateOrCreateForm
from home.models import User
from django.contrib.auth.models import UserManager

def update(request):
    
    #fazer a pertinencia de usuario para acessar essa view
    
    if request.method == 'POST':
        form = UpdateOrCreateForm(request.POST)
        context = {
        'title': 'Update',
        'form': form,
        }
        if form.is_valid():     
            ...

        url = 'home/index.html'
        return render(request, url, context=context)
        
    context = {
        'title': 'Update',
        'form': UpdateOrCreateForm(
            matricula = '000000000000',
            first_name = 'first_name',
            last_name = 'last_name',
            email = 'email@email.com',
        ),
    }
    url = 'home/update.html'
    return render(request, url, context=context)

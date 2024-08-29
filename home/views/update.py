from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.update_create_form import UpdateOrCreateForm
from django.contrib.auth.models import User

def update(request):
    
    #fazer a pertinencia de usuario para acessar essa view
    
    if request.method == 'POST':
        form = UpdateOrCreateForm(request.POST)
        context = {
        'title': 'Update',
        'form': form,
        }
        if form.is_valid():     
            #form.save()
            ...
        url = 'home/index.html'
        return render(request, url, context=context)
    
    user = User(

    )

    context = {
        'title': 'Update',
        'form': UpdateOrCreateForm(
            matricula = request.user.username,
            first_name = request.user.first_name,
            last_name = request.user.last_name,
            email = request.user.email,
        ),
    }
    url = 'home/update.html'
    return render(request, url, context=context)

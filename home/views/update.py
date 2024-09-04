from django.shortcuts import render, redirect
<<<<<<< HEAD
from home.forms.update_create_form import CreateForm, UpdateForm
from home.views import message
=======
from django.shortcuts import get_object_or_404
from home.forms.update_create_form import UpdateOrCreateForm
from django.contrib.auth.models import User
>>>>>>> f7b2d075c78c58a87b3f5bb1e4c22ee22e6f293a

def update(request):
    
    #fazer a pertinencia de usuario para acessar essa view
    
    
    if request.method == 'POST':
        form = UpdateForm(data=request.POST, instance=request.user)
        context = {
        'title': 'Update',
        'form': form,
        }
        if form.is_valid():     
            form.save()
            message(request, 'Atualizado com sucesso', sucesss=True)
        else:
            message(request, 'Erro ao atualizar', error=True)
            url = 'home/update.html'
            return render(request, url, context=context)
        url = 'home/index.html'
        return render(request, url, context=context)
<<<<<<< HEAD

    form = UpdateForm(instance=request.user)
    context = {
        'title': 'Update',
        'form': form,
=======
    
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
>>>>>>> f7b2d075c78c58a87b3f5bb1e4c22ee22e6f293a
    }
    url = 'home/update.html'
    return render(request, url, context=context)

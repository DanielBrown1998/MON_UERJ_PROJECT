from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from home.forms.update_create_form import UpdateOrCreateForm
from home.models import User


def cadastro(request):

    if request.method == 'POST':
        form = UpdateOrCreateForm(
            request.POST
        )
        if form.is_valid():
            #form.save()
            return redirect('home:home')
        context = {
        'title': 'Cadastro',
        'form': form,
        }
        url = 'home/cadastro.html'
        return render(request, url, context=context)
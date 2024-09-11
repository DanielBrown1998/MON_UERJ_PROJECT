from django.shortcuts import render, redirect
from home.forms.update_create_form import CreateForm
from home.views import message
from django.contrib.auth.models import User
from home.models import DataUser
def cadastro(request):

    if request.method == 'POST':
        print('passei aqui')
        form = CreateForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            user = User.objects.get(
                username=form.cleaned_data['username']
            )
            data_user = DataUser(owner=user)
            data_user.save()
            message(request, 'Cadastro realizado com sucesso!', sucesss=True)
            return redirect('home:home')
        message(request, 'Atente-se aos requisitos!!!')
        context = {
        'title': 'Cadastro',
        'form': form,
        }
        url = 'home/cadastro.html'
        return render(request, url, context=context)
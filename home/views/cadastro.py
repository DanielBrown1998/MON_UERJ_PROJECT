from django.shortcuts import render, redirect
from home.forms.update_create_form import CreateForm
from home.views import message

def cadastro(request):

    if request.method == 'POST':
        print('passei aqui')
        form = CreateForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            message(request, 'Cadastro realizado com sucesso!', sucesss=True)
            return redirect('home:home')
        message(request, 'Atente-se aos requisitos!!!')
        context = {
        'title': 'Cadastro',
        'form': form,
        }
        url = 'home/cadastro.html'
        return render(request, url, context=context)
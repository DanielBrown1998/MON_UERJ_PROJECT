from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.


from datetime import datetime
data = [
    {   'matricula': 201213313612,
     'nome': 'Aluno2',
     'data': datetime.now()
     },
     {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
    {   'matricula': 201213313612,
     'nome': 'Aluno2',
     'data': datetime.now()
     },
     {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },
      {   'matricula': 202113313613,
      'nome': 'Aluno1',
      'data': datetime.now()
      },

]
horario = []

def index(request):
    context = {
        'title': 'Home',
        'horas': horario
    }
    url = 'home/index.html'
    return render(request, url, context=context)

def monitoria(request):
    context = {
        'title': 'Monitoria',
        'data': data,
        }
    url = 'home/monitorias.html'
    return render(request, url, context=context)

def dados(request):
    context = {
        'title': 'Data',
        'data': data,
    }
    url = 'home/data.html'
    return render(request, url, context=context)

def cadastro(request):
    context = {
        'title': 'Cadastro',
    }
    url = 'home/cadastro.html'
    return render(request, url, context=context)
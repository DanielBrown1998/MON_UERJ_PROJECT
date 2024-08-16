
from django.shortcuts import render, redirect
from home.models import User

def cadastro(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('password2', '')
        if password != confirm_password:
            print(password, ' != ', confirm_password)
        print(username, first_name, last_name, email, password, confirm_password)
        #user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        #user.save()
        return redirect('home:login')
    return redirect('home:index')

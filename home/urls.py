from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='home'),
    path('monitorias/', views.monitoria, name='monitorias'),
    path('data/', views.dados, name='dados'),
    path('config/', views.config, name = 'config'),
    path('cadastro/', views.cadastro, name='cadastro'),
]

from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('monitorias/', views.monitoria, name='monitorias'),
    path('search/', views.search, name='search'),
    path('udpate/', views.update, name='update'),
    path('data/', views.dados, name='dados'),
    path('config/', views.config, name='config'),
    path('', views.index, name='home'),
]

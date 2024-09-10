from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    #uso livre.
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cadastro/', views.cadastro, name='cadastro'),

    path('monitorias/', views.monitoria, name='monitorias'),
    path('monitorias/search/', views.search, name='search'),

    #o usuário pode acessar.
    path('update/', views.update, name='update'),
    path('update/password/', views.password, name='password'),
    path('marcar_monitoria/', views.marcar_monitoria, name='marcar_monitoria'),

    #somente o super-user pode acessá-lo.
    path('data/', views.dados, name='dados'),
    path('config/', views.config, name='config'),
    path('config/search/', views.search_config, name='search_config'),
    path('config/update-monitoria/', views.update_monitorias, name='update_monitorias'),
    path('config/update-days/', views.update_days, name='update_days'),
    path('config/update-hours/', views.update_hours, name='update_hours'),
    path('config/matricula/', views.matricula, name='matricula'),
    path('config/matricula/create', views.create, name='create'),
    path('config/matricula/update', views.update_matricula, name='update_matricula'),
    path('config/matricula/delete', views.delete_matricula, name='delete_matricula'),
    path('config/usuarios', views.usuarios, name='usuarios'),
    path('config/usuarios/search', views.search_usuarios, name='search_usuarios'),    
    path('config/usuarios/update', views.update_usuarios, name='update_usuarios'),
]

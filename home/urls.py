from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    #uso livre
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('monitorias/', views.monitoria, name='monitorias'),
    path('search/', views.search, name='search'),

    #o usuário pode acessar
    path('udpate/', views.update, name='update'),

    #somento o superuser pode acessá-lo
    path('data/', views.dados, name='dados'),
    path('config/', views.config, name='config'),
    path('config/search/', views.search_config, name='search_config'),
    path('config/update-monitoria/', views.update_monitorias, name='update_monitorias'),
    path('config/update-days/', views.update_days, name='update_days'),
    path('config/update-hours/', views.update_hours, name='update_hours'),
    path('config/matricula/', views.matricula, name='matricula'),
    path('config/matricula/create', views.create, name='create'),
    path('config/matricula/update', views.update_matricula, name='update_matricula'),
    path('config/usuarios', views.usuarios, name='usuarios'),
    path('config/search_usuarios', views.search_usuarios, name='search_usuarios'),    

    #CRUD - todas essas views vão dentro da página config.
    #path('config/<int:id>/detail', views.detail, name='detail'),
    #path('config/<int:id>/update/', views.update, name='update_admin'),
    #path('config/<int:id>/delete/', views.delete, name='delete'),

]

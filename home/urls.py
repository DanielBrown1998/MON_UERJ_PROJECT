from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [

    #uso livre
    path('', views.index, name='home'),
    path('monitorias/', views.monitoria, name='monitorias'),
    path('search/', views.search, name='search'),
    #o usuário pode acessar
    path('udpate/', views.update, name='update'),

    #somento o superuser pode acessá-lo
    path('data/', views.dados, name='dados'),
    path('config/', views.config, name='config'),
    path('config/search/', views.search_config, name='search_config'),
    path('config/matricula/', views.matricula, name='matricula'),
    path('config/matricula/create', views.create, name='create'),
    path('config/matricula/update', views.update_matricula, name='update_matricula'),
    

    #CRUD - todas essas views vão dentro da página config.
    #path('config/<int:id>/detail', views.detail, name='detail'),
    #path('config/<int:id>/update/', views.update, name='update_admin'),
    #path('config/<int:id>/delete/', views.delete, name='delete'),

]

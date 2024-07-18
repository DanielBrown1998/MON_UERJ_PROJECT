from django.contrib import admin
from home import models


# Register your models here.

@admin.register(models.Monitorias)
class MonitoriasAdmin(admin.ModelAdmin):
    list_display = 'date', 'matricula',
    list_filter = 'date', 'matricula',
    search_fields = 'date', 'matricula',
    list_per_page = 10
    list_max_show_all = 100


@admin.register(models.Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = 'matricula', 
    list_filter = 'matricula',
    search_fields = 'matricula',
    list_per_page = 10
    list_max_show_all = 60


@admin.register(models.DataUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'matricula',
        'name', 
        'email', 
        'phone',  
        'monitorias_marcadas', 
        'monitorias_presentes',
        )
    
    ordering = 'matricula', 
    list_filter = 'monitorias_presentes',
    search_fields = 'matricula', 'name', 'email', 'phone', 'monitorias',
    list_per_page = 10
    list_max_show_all = 60
    list_editable = 'monitorias_presentes',
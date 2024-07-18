from django.contrib import admin
from home import models


# Register your models here.

@admin.register(models.Monitorias)
class MonitoriasAdmin(admin.ModelAdmin):
    list_display = 'date', 'username',
    list_filter = 'date', 'username',
    search_fields = 'date', 'username',
    list_per_page = 10
    list_max_show_all = 100


@admin.register(models.DataUser)
class DataUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'monitorias_marcadas', 'monitorias_presentes',)
    
    list_filter = 'monitorias_presentes',
    search_fields = 'username', 'first_name', 'email',
    list_per_page = 10
    list_max_show_all = 60
    list_editable = 'monitorias_presentes', 'is_staff', 'email',
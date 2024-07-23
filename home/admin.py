from django.contrib import admin
from home import models


# Register your models here.

@admin.register(models.Monitorias)
class MonitoriasAdmin(admin.ModelAdmin):
    list_display = 'date', 'owner',
    list_filter = 'date', 'owner',
    search_fields = 'date', 'owner',
    list_per_page = 10
    list_max_show_all = 100


@admin.register(models.DataUser)
class DataUserAdmin(admin.ModelAdmin):
    list_display = ('owner', 'monitorias_marcadas', 'monitorias_presentes',)
    list_filter = 'monitorias_presentes',
    list_per_page = 10
    list_max_show_all = 60
    list_editable = 'monitorias_presentes',


@admin.register(models.Horas)
class HorasAdmin(admin.ModelAdmin):
    list_display = 'time', 'day',
    list_filter = 'day',


@admin.register(models.Days)
class DaysAdmin(admin.ModelAdmin):
    list_display = 'day',

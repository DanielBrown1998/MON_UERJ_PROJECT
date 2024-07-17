from django.contrib import admin
from home import models


# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'matricula',
        'name', 
        'password', 
        'email', 
        'phone',  
        'monitorias_marcadas', 
        'monitorias_presentes',
        )


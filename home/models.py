from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    matricula = models.CharField(max_length=12, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    monitorias_marcadas = models.IntegerField(default=0)        
    monitorias_presentes = models.IntegerField(default=0)
    monitor = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class Date(models.Model):
    date = models.DateField()
    

from django.db import models
from django.utils import timezone

# Create your models here.

DEFAULT = "000000000000"
PK = True

class Matricula(models.Model):
    
    class Meta:
        verbose_name = 'Matricula'
        verbose_name_plural = 'Matriculas'
    
    matricula = models.CharField(max_length=12, primary_key=PK, default= DEFAULT)
    staff = models.BooleanField(default=False)


class DataUser(models.Model):

    class Meta:
        verbose_name = 'DataUser'
        verbose_name_plural = 'DataUsers'

    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=9)
    monitorias_marcadas = models.IntegerField(default=0)        
    monitorias_presentes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name


class Monitorias(models.Model):
    
    class Meta:
        verbose_name_plural = "Monitorias"
        unique_together = ('date', 'matricula'),

    date = models.DateField()
    matricula = models.ForeignKey(Matricula, on_delete=models.DO_NOTHING)

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class DataUser(models.Model):

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    monitorias_marcadas = models.IntegerField(default=0)        
    monitorias_presentes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.owner.first_name + self.owner.last_name


class Monitorias(models.Model):
    
    date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
 
    class Meta:
        verbose_name_plural = "Monitorias"
        unique_together = ('date', 'owner'),


class Days(models.Model):

    class Meta:
        verbose_name = "Dia"
        verbose_name_plural = "Dias"

    day = models.CharField(max_length=20)


class Horas(models.Model):

    class Meta:
        verbose_name = "Hora"
        verbose_name_plural = "Horas"
        unique_together = 'time', 'day'

    time = models.TimeField()
    day = models.ForeignKey(Days, on_delete=models.CASCADE)

from django.db import models

# Create your models here.


class Configuraciones(models.Model):
    id_configuraciones=models.AutoField(primary_key=True)
    act_wifi = models.BooleanField()
    mail = models.CharField(max_length=100)
    reiniciar = models.BooleanField()
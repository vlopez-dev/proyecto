from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_invernadero= models.ForeignKey(invernadero:invernadero,)
    id_cliente = models.AutoField(primary_key=True)
    broker_conexion = models.CharField(max_length=100)
    
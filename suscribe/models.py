from django import forms
from django.db import models

from cliente.models import Cliente


# Create your models here.




MODELOSENSOR = [
            ('/dht/temperatura', 'DHT 11 Temperatura'),

            ('/dht/humedad', 'DHT 11 Humedad'),
            
        ]



class Suscribe(models.Model):
    id_cliente= models.name = models.ForeignKey('cliente.Cliente',on_delete=models.CASCADE)

    ruta = models.CharField(primary_key=True ,max_length=50,choices=MODELOSENSOR,default='/dht/temperatura')
    valor_activo=models.FloatField()
    actuador= models.CharField(max_length=50,null=True)
    valor_actuador= models.BooleanField()

    def add(self):
        self.save


    def __str__(self):
        return self.id_cliente



# class Sensormodelo(models.Model):
    



class Lectura(models.Model):
    ruta = models.ForeignKey(Suscribe, on_delete=models.CASCADE)
    lectura_sensor= models.FloatField()
    lectura_fecha= models.DateTimeField(auto_now_add=True)
    



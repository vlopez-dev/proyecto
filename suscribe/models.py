from django.db import models

# Create your models here.
class Suscribe(models.Model):
    id_suscribe = models.AutoField(primary_key=True)
    ruta = models.CharField(max_length=50)
    tipo = models.CharField(max_length=10)
    
 
 
 
 
 
 
 

class Lectura(models.Model):
    suscribe = models.ForeignKey(Suscribe, on_delete=models.CASCADE)

    id_lectura= models.AutoField(primary_key=True)
    lectura_sensor= models.CharField(max_length=8,blank=True)
    lectura_fecha= models.DateTimeField(auto_now_add=True)
    
    
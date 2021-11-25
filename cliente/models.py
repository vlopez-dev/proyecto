from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_conexion= models.CharField(max_length=50)
    id_invernadero= models.name = models.ForeignKey('invernadero.Invernadero',on_delete=models.CASCADE)
    id_cliente = models.AutoField(primary_key=True)
    broker_conexion = models.CharField(max_length=100)
    
    
    
    
    
    
    

    def add(self):
        self.save


    def __str__(self):
        return self.nombre_conexion

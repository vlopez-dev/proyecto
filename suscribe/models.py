from django.db import models

# Create your models here.
class Suscribe(models.Model):
    ruta = models.CharField(primary_key=True ,max_length=50)
    tipo = models.CharField(max_length=15)
    valor_activo=models.FloatField()
    actuador= models.CharField(max_length=50,null=True)
    valor_actuador= models.BooleanField()

    def add(self):
        self.save


    def __str__(self):
        return self.ruta



class Lectura(models.Model):
    ruta = models.ForeignKey(Suscribe, on_delete=models.CASCADE)
    lectura_sensor= models.FloatField()
    lectura_fecha= models.DateTimeField(auto_now_add=True)
    



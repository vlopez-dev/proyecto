from django.db import models

# Create your models here.
class Suscribe(models.Model):
    #id_suscribe = models.AutoField(primary_key=True)
    ruta = models.CharField(primary_key=True ,max_length=50)
    tipo = models.CharField(max_length=15)
    valor_activo=models.FloatField()
    actuador= models.CharField(max_length=50,null=True)


    def add(self):
        self.save


    def __str__(self):
        return self.ruta



class Lectura(models.Model):
    ruta = models.ForeignKey(Suscribe, on_delete=models.CASCADE)
    lectura_sensor= models.FloatField()
    lectura_fecha= models.DateTimeField(auto_now_add=True)


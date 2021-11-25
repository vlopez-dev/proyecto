from django.db import models

# Create your models here.
class Invernadero(models.Model):
    id_invernadero=models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)



    def add(self):
        self.save


    def __str__(self):
        return self.nombre

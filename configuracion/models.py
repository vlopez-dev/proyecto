from django.db import models

# Create your models here.
class Configuracion(models.Model):
    id_configuracion= models.AutoField(primary_key=True)
    email=models.CharField(max_length=100)
    passw= models.CharField(max_length=100)
    mail_cuenta = models.CharField(max_length=100)
    receptor_mail= models.CharField(max_length=100)
    
from django.db import models







SERVER = [
            ('smtp.gmail.com: 587', 'Gmail'),
            
          
            
        ]

# Create your models here.
class Configuracion(models.Model):
    id_configuracion= models.AutoField(primary_key=True)
    email_from=models.CharField(max_length=100)
    passw_from= models.CharField(max_length=100)
    email_to = models.CharField(max_length=100)
    server_config= models.CharField(max_length=100,choices=SERVER,default='smtp.gmail.com: 587')
    
    
    
    

    def add(self):
        self.save


    def __str__(self):
        return self.email_from

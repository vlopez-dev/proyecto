from django.shortcuts import render,redirect
from django.db import models
from .models import Invernadero
from .forms import InvernaderoForm
import paho.mqtt.client as mqttClient
import time
import threading
from suscribe.models import Lectura, Suscribe

# Create your views here.








def invernadero_home(request):

    return render(request,'invernadero/home.html')






def invernadero_agregar(request):
    if request.method=="GET":
        form =InvernaderoForm()
    
        return render(request,'invernadero/agregar.html',{'form':form})

    else:
        form =InvernaderoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cliente/agregar/')
    

    
    


def listar_invernadero(request):
    invernaderos = Invernadero.objects.all()

    return render(request,'invernadero/listar.html',{'invernadero':invernaderos})





def obtener_lectura(request):
    ob = Lectura.objects.last() 
    lectura=ob.lectura_sensor
    print("variable para la view", str(lectura))
    return render(request, 'invernadero/home.html',{'lectura_sensor':lectura} )

# Falta que muestre el valor en html

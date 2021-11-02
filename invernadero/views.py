from django.shortcuts import render,redirect
from django.db import models
from .models import Invernadero
from .forms import InvernaderoForm
import paho.mqtt.client as mqttClient
import time
import threading
# Create your views here.





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

    return render(request,'invernadero/inver_list.html',{'invernadero':invernaderos})

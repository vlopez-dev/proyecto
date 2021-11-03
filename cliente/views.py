from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm
import paho.mqtt.client as mqttClient
import threading
import time

# Create your views here.



def cliente_agregar(request):
    if request.method=="GET":
        form = ClienteForm()
    
        return render(request,'cliente/agregar.html',{'form':form})

    else:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/suscribe/agregar/')
    

    
    
    
    


def listar_clientes(request):
    clientes = Cliente.objects.all()

    return render(request,'cliente/listar.html',{'cliente':clientes})

    
    
    
    
    
    
    
    
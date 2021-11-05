import json

from django.shortcuts import render,redirect
from django.db import models

from .models import Invernadero
from .forms import InvernaderoForm
import paho.mqtt.client as mqttClient
import time
import threading
from suscribe.models import Lectura, Suscribe
# Create your views here.
from django.http import JsonResponse







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




def obtener_datos(request):
    valores = Lectura.objects.last()   
    # Filtro el ultimo objeto lectura y lo guardo para crearon un json
    data = {
        'temperatura': valores.lectura_sensor,
        'ruta'       : valores.ruta_id
        }
    print(data)
    return JsonResponse(data)


def obtener_rutas(request):
    suscribes = Suscribe.objects.all()
    
    return render(request,'invernadero/home.html',{'suscribe':suscribes})

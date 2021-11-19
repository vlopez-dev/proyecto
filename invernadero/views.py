import json
from django.forms.models import model_to_dict

from django.shortcuts import render,redirect
from django.db import models
from django.contrib import messages

from .models import Invernadero
from .forms import InvernaderoForm
import paho.mqtt.client as mqttClient
import time
import threading
from suscribe.models import Lectura, Suscribe
# Create your views here.
from django.http import JsonResponse
from notifypy import Notify






# Retorno todos los suscribptores para crear las card
def invernadero_home(request):
 context = {'home': Suscribe.objects.all()}
 return render(request, "invernadero/home.html", context)

    # return render(request,'invernadero/home.html')











def invernadero_agregar(request,id_invernadero=0):
    if request.method == "GET":
        if id_invernadero == 0 :
            form = InvernaderoForm()
        else:
            invernadero = Invernadero.objects.get(pk=id_invernadero)
            #invernadero = Invernadero.objects.filter(pk=id_invernadero).first()

            form = InvernaderoForm(instance=invernadero)
        return render(request, 'invernadero/agregar.html', {'form': form})
    else:
        if id_invernadero == 0:
            form = InvernaderoForm(request.POST)
        else:
            invernadero = Invernadero.objects.get(pk=id_invernadero)
            form = InvernaderoForm(request.POST,instance= invernadero)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')
            

        return redirect('/listar/')





def listar_invernadero(request):
    context = {'listar_invernadero': Invernadero.objects.all()}
    return render(request, "invernadero/listar.html", context)






def obtener_datos(request):
    valores = Lectura.objects.last()
    # valores=Lectura.objects.filter(ruta_id='esp/dht/temperature').last()
    # valores=Lectura.objects.filter(ruta_id='esp/dht/humidity').last()


    # Filtro el ultimo objeto lectura y lo guardo para crearon un json

    data = {
            'temperatura': valores.lectura_sensor,
            'ruta'       : valores.ruta_id,
            }
    
           
    print(data)
    return JsonResponse(data)








def obtener_rutas(request):
    # time.sleep(15)
    suscribes = Suscribe.objects.all()
    return render(request,'invernadero/home.html',{'suscribe':suscribes})








def invernadero_delete(request,id_invernadero):
    
    invernadero = Invernadero.objects.get(pk=id_invernadero)
    invernadero.delete()
    messages.add_message(request, messages.INFO, 'Eliminado correctamente!.')

    return redirect('/listar')





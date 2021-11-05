from urllib import request
from django.http.response import JsonResponse
from django.utils import timezone
import datetime
from django.utils.timezone import make_aware
from urllib.request import Request
from django.shortcuts import render, redirect
import suscribe
from suscribe.models import Lectura, Suscribe
from .forms import SuscribeForm
import time
import threading
from cliente.models import Cliente
import paho.mqtt.client as mqttClient
import json



    




# ----------------------------------------------------------------------------
def suscripcion_agregar(request):
    if request.method == "GET":
        form = SuscribeForm()
        return render(request, 'suscribe/agregar.html', {'form': form})
    else:
        form = SuscribeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/invernadero/home/')

# -------------------------------------------------------------------------------







# --------------------------------------------------------------------------------

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
         + message.topic + "' with QoS " + str(message.qos))
    #print("Mensaje recibido =", str(message.payload.decode("utf-8")))
    mensaje = float(message.payload.decode("utf-8"))
    #print("Este es el qos" + str(message.qos))
    print(message.topic)
    # varificar_umbral(mensaje)
    # if mensaje >25:
    #     enviar_mail()
    # obverificartemp = Lectura.objects.latest('lectura_sensor')
# Sirve cambiar el mensaje de string a integer para hacer comparaciones apenas pase por el bucle


    ob = Lectura.objects.create( ruta_id=message.topic, lectura_sensor=mensaje)
    ob.save()
    time.sleep(1)

# --------------------------------------------------------------------------------






Connected = False  # Variable golabal de conexion







def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        global Connected
        Connected = True
    else:
        print("Fallo la conexion")




# --------------------------------------------------------------------------------



# --------------------------------------------------------------------------------


def conexion_broker():
    Connected = False  # global variable for the state of the connection
print("Contado al broker")
broker_address = "inversoft.ddns.net"
# objeto = Cliente.objects.all()
# for i in objeto:
#     broker_address= i.broker_conexion
# direccion AP broker "10.3.141.1"
port = 1883  # Broker port
user = "proyecto"  # Connection username
password = "proyecto"  # Connection password
client = mqttClient.Client("Python")
client.username_pw_set(user, password=password) 
client.on_connect = on_connect  
client.on_message = on_message  
client.connect(broker_address, port=port) 
client.loop_start()  # start the loop
print("ejecute el loop de conexion")



# --------------------------------------------------------------------------------







# --------------------------------------------------------------------------------


def subscribing():
    while Connected != True:  # Wait for connection
        time.sleep(1)
        ob = Suscribe.objects.all()
        for i in ob:
                client.subscribe(i.ruta)  #Linea de suscricion original
sub = threading.Thread(target=subscribing)
sub.start()
time.sleep(1)




# --------------------------------------------------------------------------------

                # Vericar valor actividad
                
def varificar_umbral(lectura):
    ob = Suscribe.objects.all()
    for i in ob:
        umbral = i.valor_acti
       
        if lectura > umbral:
            # "21"       "20"
            enviar_mail()
            print(" Activando mail y acciones")
            
        else:
            print("No se toman acciones el umbral es correcto")
        
# Verificado el funcionamiento del umbral, falta agregar la ruta del actuador y filtrar la ruta del sensor asociado












# --------------------------------------------------------------------------------
def listar_suscripciones(request):
    suscribes = Suscribe.objects.all()
    return render(request,'suscribe/listar.html',{'suscribe':suscribes})





# --------------------------------------------------------------------------------


# --------------------------------------------------------------------------------



# def reporte(request):
#     lecturas=Lectura.objects.filter(lectura_fecha =["2021-01-01", "2021-01-31"])

#     # lecturas=Lectura.objects.filter(lectura_fecha ='2021-01-01','lectura_fecha'='2021-12-31')
#     print(lecturas)
#     return render(request,'suscribe/reporte.html',{'lectura':lecturas})



# --------------------------------------------------------------------------------




# --------------------------------------------------------------------------------

# ENVIO DE MAILS



def enviar_mail():
     
    print("mail enviado")
    
    
    
    
    
    
    """ 
    
def obtener_datos(request):
    #Se invoca al metodo del modelo sense hat

    #Se obtiene ultimo valor ingresado en BD
    valores = Lectura.objects.last()   

    #Se crea objeto JSON
    data = {
        'temp': valores.lectura_sensor,
        }
    print(data)
    return JsonResponse(data) """

from urllib.request import Request
from django.shortcuts import render,redirect

from suscribe.models import  Lectura, Suscribe

from .forms import SuscribeForm
import time
import threading
from cliente.models import Cliente
import paho.mqtt.client as mqttClient

# Create your views here.



def suscripcion_agregar(request):
    if request.method=="GET":
        form = SuscribeForm()
    
        return render(request,'suscribe/agregar.html',{'form':form})

    else:
        form = SuscribeForm(request.POST)
        if form.is_valid():
            # ruta=form.cleaned_data.get("ruta","id_suscribe")
            # print(ruta)
            # subscribing(ruta="esp/dht/temperature",id_suscribe=1)
            
            form.save()
            

        return redirect('/suscribe/home.html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    







def on_message(client, userdata, message):
    print("Mensaje recibido =",str(message.payload.decode("utf-8")))
    mensaje = str(message.payload.decode("utf-8"))
    ob = Suscribe.objects.all()
    for i in ob:
        id_suscribe=i.id_suscribe
        print(id_suscribe)
    
    
    
    
    
    
    
    ob= Lectura.objects.create(suscribe_id=id_suscribe,lectura_sensor=mensaje)
    print("creo objecto para guardar lectura")
    # ob.lectura_sensor= mensaje
    ob.save()
    # Suscribe.objects.create(mensaje)    
    time.sleep(1)






Connected = False   #Variable golabal de conexion

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        global Connected                
        Connected = True               
        # subscribing()
    else:
        print("Fallo la conexion") 







def conexion_broker():
    Connected = False   #global variable for the state of the connection
print("Contado al broker")
broker_address="inversoft.ddns.net"
# objeto = Conexion.objects.last()
# broker=objeto.broker_conexion
# print(broker)
# broker_address= broker
#direccion AP broker "10.3.141.1"
port = 1883                         #Broker port
user = "proyecto"                    #Connection username
password = "proyecto"            #Connection password
client = mqttClient.Client("Python") 
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                     #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
print("ejecute el loop de conexion")



    
    
    
       
def subscribing():
    ruta=""
    while Connected != True:    #Wait for connection
        time.sleep(1)
        
        ob = Suscribe.objects.all() #Busco todos los objetos en la tabla suscribe y los recorro uno suscribiendome al sensor
        for i in ob:                        
            ruta=i.ruta
            if ruta =="":
                pass
            
            else:
                client.subscribe(ruta) 
    #client.subscribe("esp/dht/temperature")  #Linea de suscricion original
sub=threading.Thread(target=subscribing)
sub.start()
time.sleep(1)
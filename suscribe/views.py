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



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

    




# ---------------------------Metodo del form agregar-------------------------------------------------
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







# ------------------------Metodo que recibe el mensaje desde el nodemcu--------------------------------------------------------

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '"
         + message.topic + "' with QoS " + str(message.qos))
                                                                                     #print("Mensaje recibido =", str(message.payload.decode("utf-8")))
    mensaje = float(message.payload.decode("utf-8"))
                                                                                          #print("Este es el qos" + str(message.qos))
    print(message.topic)
    varificar_umbral(mensaje)
    ob = Lectura.objects.create( ruta_id=message.topic, lectura_sensor=mensaje)
    ob.save()
    time.sleep(1)                                                                                    # if mensaje <20:
                                                                                        #     enviar_mail()
                                                                                        #     on_publish
                                                                                        # obverificartemp = Lectura.objects.latest('lectura_sensor')
                                                                                        # Sirve cambiar el mensaje de string a integer para hacer comparaciones apenas pase por el bucle

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



# ---------------------------------Conexion al broker-----------------------------------------------


def conexion_broker():
    Connected = False  # global variable for the state of the connection
print("Contado al broker")
# broker_address = "inversoft.ddns.net"
objeto = Cliente.objects.all()
for i in objeto:
    broker_address= i.broker_conexion
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

# Falta verificar cuando la conexion es vacia

# --------------------------------------------------------------------------------







# -----------------------------Metodo suscripcion---------------------------------------------------


def subscribing():
    while Connected != True:  # Wait for connection
        time.sleep(1)
        ob = Suscribe.objects.all()
        for i in ob:
                client.subscribe(i.ruta)  #Linea de suscricion original
sub = threading.Thread(target=subscribing)
sub.start()
time.sleep(1)




# ----------------------------------Metodo pubicador----------------------------------------------------


  
def on_publish(client,userdata,result,actuador):             #create function for callback
    print("data published \n")
    pass
    
# client1= mqttClient("control1")                           #create client object
    client.on_publish = on_publish                          #assign function to callback
# client1.connect(broker,port)
# #establish connection
    print("Haciendo publicacion")
    # ret= client.publish("esp/test","#off")   
    ret= client.publish(actuador,"#on")   


# Falta dar la opcion de on /off

# --------------------------------------------------------------------------------------








# ------------------------------Verificacion de valores de activacion--------------------------------------------------

                # Vericar valor actividad
                
def varificar_umbral(lectura):
    ob = Suscribe.objects.all()
    for i in ob:
        ruta = i.ruta
        actuador = i.actuador
        umbral = i.valor_activo

        if lectura > umbral:
            # "18"       "16"
            # enviar_mail()
            on_publish(actuador)
            print(" Activando mail y acciones")
            
        else:
            print("No se toman acciones el umbral es correcto")
        
# Verificado el funcionamiento del umbral, falta agregar la ruta del actuador y filtrar la ruta del sensor asociado












# ---------------------------------Reporte suscripciones-----------------------------------------------
def listar_suscripciones(request):
    suscribes = Suscribe.objects.all()
    return render(request,'suscribe/listar.html',{'suscribe':suscribes})





# --------------------------------------------------------------------------------













# -----------------------Reporte por fechas---------------------------------------------------------



# def reporte(request):
#     lecturas=Lectura.objects.filter(lectura_fecha =["2021-01-01", "2021-01-31"])

#     # lecturas=Lectura.objects.filter(lectura_fecha ='2021-01-01','lectura_fecha'='2021-12-31')
#     print(lecturas)
#     return render(request,'suscribe/reporte.html',{'lectura':lecturas})



# --------------------------------------------------------------------------------





















# --------------------------------------------------------------------------------

# ENVIO DE MAILS



def enviar_mail():
    
    msg = MIMEMultipart()
 
    #Mensaje
    message = "Test invernadero"
    
    
    #Parametros para el envio de mensajes
    password = "gdi092021"
    msg['From'] = "gdinverna092021@gmail.com"
    msg['To'] = "victorl_222@hotmail.com"
    msg['Subject'] = "Test"
    
    msg.attach(MIMEText(message, 'plain'))

    #Creo el servidor
    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    #Login con las credenciales
    server.login(msg['From'], password)
    
    #Envio el mail por medio del servidor
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    #Salgo
    server.quit()
    # Imprimo un mensaje de enviado
    print ("Mensaje enviado a : %s:" % (msg['To']))
        
    print("mail enviado")
    
    
    
    # Se deberia crear otra app que solo envie los mails y asi dar la posibilidad de
    # configurar el mail
from urllib import request
from django.http.response import JsonResponse
from django.utils import timezone
import datetime
from django.utils.timezone import make_aware
from urllib.request import Request
from django.shortcuts import render, redirect
import suscribe
from suscribe.models import Lectura, Suscribe
from django.contrib import messages
from .forms import SuscribeForm,LecturasForm
import time
import threading
from cliente.models import Cliente
import paho.mqtt.client as mqttClient
import json
from notifypy import Notify
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger



from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
client = mqttClient.Client("Python")

    

# ----------------------------------Metodo para agregar suscriptor--------------------------------------------------------------


def suscripcion_agregar(request,ruta=""):
    if request.method == "GET":
        if ruta == "" :
            form = SuscribeForm()
        else:
            suscribe = Suscribe.objects.get(pk=ruta)
            #invernadero = Invernadero.objects.filter(pk=id_invernadero).first()

            form = SuscribeForm(instance=suscribe)
        return render(request, 'suscribe/agregar.html', {'form': form})
    else:
        if ruta == "":
            form = SuscribeForm(request.POST)
        else:
            suscribe = Suscribe.objects.get(pk=ruta)
            form = SuscribeForm(request.POST,instance= suscribe)
        if form.is_valid():
            form.save()
        messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

        return redirect('/suscribe/listar/')

# -------------------------------------------------------------------------------------------------------






# ---------------------------------Metodo listar para la vista----------------------------------------------------------------------

def listar_suscribe(request):
    context = {'listar_suscribe': Suscribe.objects.all()}
    return render(request, "suscribe/listar.html", context)




# -------------------------------------------------------------------------------------------------------------------------------------






# -----------------------------------------Metodo para eliminar una suscripcion -----------------------------------------------------------------------------------------------


def suscribe_delete(request,ruta):
    
    suscribe = Suscribe.objects.get(pk=ruta)
    suscribe.delete()
    messages.add_message(request, messages.INFO, 'Eliminado correctamente!.')

    return redirect('/suscribe/listar/')


# --------------------------------------------------------------------------------------------------------------------------------------













# ------------------------Metodo que recibe el mensaje desde el nodemcu--------------------------------------------------------

def on_message(client, userdata, message):
    print("estoy en on message")
    print("Received message '" + str(message.payload) + "' on topic '"
         + message.topic + "' with QoS " + str(message.qos))
    topic=message.topic
    mensaje = float(message.payload.decode("utf-8"))
    print("Recibiendo mensaje"+message.topic)
    varificar_umbral(mensaje,topic)
    time.sleep(1)

    ob = Lectura.objects.create(ruta_id=message.topic, lectura_sensor=mensaje)
    ob.save()

# --------------------------------------------------------------------------------














Connected = False  # Variable golabal de conexion




# --------------------------------------Metodo para verificar la conexion al broker-----------------------------------------------


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado al broker")
        Connected = True
    else:
        print("Fallo la conexion")




# --------------------------------------------------------------------------------








# ---------------------------------Conexion al broker-----------------------------------------------


# def conexion_broker():
#     Connected = False  
# print("Contado al broker")
# broker_address = "192.168.1.100"

# port = 1883  # Broker port
# user = "proyecto"  # Connection username
# password = "proyecto"  # Connection password
# client = mqttClient.Client("Python")
# client.username_pw_set(user, password=password) 
# client.on_connect = on_connect
# client.on_message = on_message

# client.connect(broker_address, port=port) 
# client.loop_start()  # start the loop
# print("ejecute el loop de conexion")

    # Falta verificar cuando la conexion es vacia

# --------------------------------------------------------------------------------

# -----------------------------------------------------








# --------------Funcion con cambio de tiempo en el guardado con error--------------------------------------

    Connected = True  
print("Contado al broker")
# broker_address = "inversoft.ddns.net"
broker_address=""


objeto = Cliente.objects.all()

for i in objeto:
    broker_address= i.broker_conexion
    print("entre al for conexion")
port = 1883  # Broker port
user = "proyecto"  # Connection username
password = "proyecto"  # Connection password
client = mqttClient.Client("Python")
client.username_pw_set(user, password=password) 
client.on_connect = on_connect
client.on_message = on_message
if broker_address=="" or None:
   pass
else:
    client.connect(broker_address, port=port) 
    client.loop_start()  # start the loop
    print("ejecute el loop de conexion")

    # Falta verificar cuando la conexion es vacia

# --------------------------------------------------------------------------------










# --------------------------------------------------




# -----------------------------Metodo suscripcion---------------------------------------------------


def subscribing():
    while Connected != True:  # Wait for connection
        # time.sleep(1)
        ob = Suscribe.objects.all()
        for i in ob:
                client.subscribe(i.ruta)  #Linea de suscricion original
sub = threading.Thread(target=subscribing)
sub.start()


# ---------------------------------------------------------------------------------------------------




# ------------------------------Verificacion de valores de activacion--------------------------------------------------



def varificar_umbral(lectura,topic):
    ob = Suscribe.objects.all()
    for i in ob:
    
        ruta = i.ruta
        actuador = i.actuador
        umbral = i.valor_activo
        if topic==ruta and lectura > umbral and actuador != None:
                        # "19"       "20"
            
            client.on_publish
            ret= client.publish(actuador,"#on")
            
            print(ret)
            print(" Activando mail y enviando accion al actuador")
            notification = Notify()
            notification.title = "Cool Title"
            notification.message = "Activando envio de mail y enviando accion al actuador."
            notification.send()
            # resultado=enviar_mail()
            # print("Resultado envio mail" +str(resultado))
        elif topic==ruta and lectura < umbral and actuador!=None:
                client.on_publish

                ret=client.publish(actuador,"#off")
                print("enviando mensaje en off")
        else:

            print("No se toman acciones el umbral es correcto")
            notification = Notify()
            notification.title = "Verificación de umbral"
            notification.message = "No se toman acciones el umbral es correcto."
            notification.send()





# -----------------------------------------------------------------------





# ---------------------------------Reporte suscripciones-----------------------------------------------
def listar_suscripciones(request):
    suscribes = Suscribe.objects.all()
    return render(request,'suscribe/listar.html',{'suscribe':suscribes})





# --------------------------------------------------------------------------------





def filtro_fechas(request):
     if request.method=="GET":
        form =LecturasForm()
        return render(request,'suscribe/filtro_fechas.html',{'form':form})
     else:
         form= LecturasForm(request.POST)
         if form.is_valid():
            dia_desde = form.cleaned_data['dia_desde']
            print(dia_desde)
            dia_hasta = form.cleaned_data['dia_hasta']
            print(dia_hasta)
            nuevofinal = dia_hasta + datetime.timedelta(days=1)

            lecturas_list=Lectura.objects.filter(lectura_fecha__range=[dia_desde, nuevofinal]).order_by('lectura_fecha')
            
            page = request.GET.get('page', 1)
            paginator=Paginator(lecturas_list,10)
            try:
                lecturas = paginator.page(page)
            except PageNotAnInteger:
                lecturas=paginator.page(1)
            except EmptyPage:
                lecturas = paginator.page(paginator.num_pages)
            

            

            return render(request, 'suscribe/reporte.html',{'lecturas': lecturas})
            # Problemas en la paginacion







# -----------------------Reporte por fechas---------------------------------------------------------



def reportes(request):

    return render(request,'suscribe/reportes.html')



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
            return True
            

    # Se deberia crear otra app que solo envie los mails y asi dar la posibilidad de
    # configurar el mail
# ----------------------------------------------------------------------------------



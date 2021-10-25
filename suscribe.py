import paho.mqtt.client as mqttClient
# import threading

import time
  
def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")  
  

    print("Sali de la funcion de conectar")




def on_message(client, userdata, message):
    print("Entre a la funcion por el mensaje")
    #print ("Message received: "  + message.payload)
    print("received message =",str(message.payload.decode("utf-8")))

    

  
Connected = False   #global variable for the state of the connection
  
broker_address= "192.168.1.100"  #Broker addressls
#direccion AP broker "10.3.141.1"
port = 1883                         #Broker port
user = "proyecto"                    #Connection username
password = "proyecto"            #Connection password
client = mqttClient.Client("Python") 
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(1)
    
client.subscribe("esp/dht/temperature")

  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print ("exiting")
    client.disconnect()
    client.loop_stop()

import paho.mqtt.client as paho
broker="192.168.1.100"
port=1883
user="proyecto"
password="proyecto"

def on_publish(client,userdata,result):             #create function for callback
    print("data published \n")
    pass
client1= paho.Client("control1")                           #create client object
client1.on_publish = on_publish                          #assign function to callback
client1.connect(broker,port)                                 #establish connection
ret= client1.publish("esp/test","#off")                   #publish







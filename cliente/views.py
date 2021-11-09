from django.shortcuts import render,redirect
from .models import Cliente
from .forms import ClienteForm
import paho.mqtt.client as mqttClient
import threading
import time
from django.contrib import messages

# Create your views here.



# def cliente_agregar(request):
#     if request.method=="GET":
#         form = ClienteForm()
    
#         return render(request,'cliente/agregar.html',{'form':form})

#     else:
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('/suscribe/agregar/')
    
    
    
    
    

def cliente_agregar(request,id_cliente=0):
    if request.method == "GET":
        if id_cliente == 0 :
            form = ClienteForm()
        else:
            cliente = Cliente.objects.get(pk=id_cliente)

            form = ClienteForm(instance=cliente)
        return render(request, 'cliente/agregar.html', {'form': form})
    else:
        if id_cliente == 0:
            form = ClienteForm(request.POST)
        else:
            cliente = Cliente.objects.get(pk=id_cliente)
            form = ClienteForm(request.POST,instance= cliente)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')
            
        return redirect('/cliente/listar/')


    
    
    
    
    

    
    
    
    


# def listar_clientes(request):
#     clientes = Cliente.objects.all()

#     return render(request,'cliente/listar.html',{'cliente':clientes})
def listar_cliente(request):
    context = {'listar_cliente': Cliente.objects.all()}
    return render(request, "cliente/listar.html", context)






def cliente_delete(request,id_cliente):
    
    cliente = Cliente.objects.get(pk=id_cliente)
    cliente.delete()
    messages.add_message(request, messages.INFO, 'Eliminado correctamente!.')

    return redirect('/cliente/listar/')

from django.shortcuts import render,redirect

from .models import Configuracion

from .forms import ConfiguracionForm
from django.contrib import messages

# Create your views here.





def configuracion_agregar(request,id_configuracion=0):
    if request.method == "GET":
        if id_configuracion == 0 :
            form = ConfiguracionForm()
        else:
            configuracion = Configuracion.objects.get(pk=id_configuracion)

            form = ConfiguracionForm(instance=configuracion)
        return render(request, 'configuracion/configmail.html', {'form': form})
    else:
        if id_configuracion == 0:
            form = ConfiguracionForm(request.POST)
        else:
            configuracion = Configuracion.objects.get(pk=id_configuracion)
            form = ConfiguracionForm(request.POST,instance= configuracion)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

        return render(request, 'configuracion/configmail.html', {'form': form})





def configuraciones_home(request):
 return render(request, "configuracion/configuraciones.html")



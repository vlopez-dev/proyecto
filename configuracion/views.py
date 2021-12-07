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

        return redirect('/configuraciones/listar/')







def configuraciones_home(request):
 return render(request, "configuracion/configuraciones.html")






def configuraciones_listar(request):
    context = {'listar_config': Configuracion.objects.all()}
    return render(request, "configuracion/listar.html", context)








def configuraciones_delete(request,id_configuracion):
    configuracion = Configuracion.objects.get(pk=id_configuracion)
    configuracion.delete()
    messages.add_message(request, messages.INFO, 'Eliminado correctamente!.')

    return redirect('/configuraciones/listar')









def configuraciones_pi(request):
 return render(request, "configuracion/config_broker.html")



def rasp_ap(request):
    return redirect("https//google.com/")
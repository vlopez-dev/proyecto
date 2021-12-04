from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
path("configuraciones_home",views.configuraciones_home,name='configuraciones_home'),
path("configmail",views.configuracion_agregar,name='configmail'),


]
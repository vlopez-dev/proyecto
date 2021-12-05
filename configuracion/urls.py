from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
path("configuraciones_home",views.configuraciones_home,name='configuraciones_home'),
path("configmail",views.configuracion_agregar,name='configmail'),
path("listar/",views.configuraciones_listar,name='listar_config'),
path('delete/<int:id_configuracion>/',views.configuraciones_delete,name='configuracion_delete'),
path('<int:id_configuracion>/',views.configuracion_agregar,name='config_update'),

path("configuraciones_pi",views.configuraciones_pi,name='configuraciones_pi'),


]
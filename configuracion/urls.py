from django.urls import path
from django.conf.urls import include, url
from . import views


urlpatterns = [
path("configuraciones",views.configuracion_agregar,name='configuraciones'),

]
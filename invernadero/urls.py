from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path("agregar/",views.invernadero_agregar,name='inv_agregar'),
    path("listar/",views.listar_invernadero,name='listar'),

    path("",views.invernadero_home,name='home'),
    url(r'^$', views.obtener_datos, name = "obtener_datos"),


    
]
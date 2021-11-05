from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    
    path("listar/",views.listar_suscripciones,name='listar'),



    
]
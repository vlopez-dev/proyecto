from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    
    path("listar/",views.listar_suscripciones,name='listar_suscribe'),
    # path("lecturas/",views.,name='lecturas'),


    # url(r'^$', views.obtener_datos, name = "home"),


    
]
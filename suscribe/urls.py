from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    
    path("listar/",views.listar_suscripciones,name='listar'),
    path("reporte/",views.reporte,name='reporte'),
    # path("obtener_valores/",views.obtener_valores,name='obtener_valores'),



    
]
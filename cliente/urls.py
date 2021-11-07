from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.cliente_agregar,name='cli_agregar'),
    path("listar/",views.listar_clientes,name='listar_cliente'),


    
]
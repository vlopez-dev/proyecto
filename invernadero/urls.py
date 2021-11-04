from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.invernadero_agregar,name='inv_agregar'),
    path("listar/",views.listar_invernadero,name='listar'),

    path("",views.invernadero_home,name='home'),
    path(" ",views.obtener_lectura,name='home'),


    
]
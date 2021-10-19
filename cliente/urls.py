from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.cliente_agregar,name='agregar'),


    
]
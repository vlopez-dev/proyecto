from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='agregar'),


    
]
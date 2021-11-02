from django.urls import path
from . import views

urlpatterns = [
    path("",views.invernadero_agregar,name='agregar'),


    
]
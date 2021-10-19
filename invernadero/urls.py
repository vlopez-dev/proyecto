from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.invernadero_agregar,name='agregar'),


    
]
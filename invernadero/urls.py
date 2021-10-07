from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("agregar/",views.invernadero_agregar,name='agregar'),
    path("listar/",views.listar_invernadero,name='listar'),

    
]
from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    path("listar/",views.listar_suscribe,name='listar_suscribe'),


    path('delete/<path:ruta>/',views.suscribe_delete,name='suscribe_delete'),
    path('<path:ruta>/', views.suscripcion_agregar,name='suscribe_update'), 


]
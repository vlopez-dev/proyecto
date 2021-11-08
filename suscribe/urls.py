from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    
    path("listar/",views.listar_suscripciones,name='listar_suscribe'),
    
    path('delete/<int:id_suscribe>/',views.suscribe_delete,name='suscribe_delete'),
    path('<int:id_suscribe>/', views.suscripcion_agregar,name='suscribe_update'), # get and post req. for update operation


    # path("lecturas/",views.,name='lecturas'),


    # url(r'^$', views.obtener_datos, name = "home"),


    
]
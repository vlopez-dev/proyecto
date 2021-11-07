from django.urls import path
from django.conf.urls import include, url

from . import views

urlpatterns = [
    path("agregar/",views.invernadero_agregar,name='inv_agregar'),
    
    path("listar/",views.listar_invernadero,name='listar'),
    
    path("valores/",views.obtener_datos,name='valores'),
    
    path('delete/<int:id_invernadero>/',views.invernadero_delete,name='invernadero_delete'),
    path('<int:id_invernadero>/', views.invernadero_agregar,name='invernadero_update'), # get and post req. for update operation

    
    path("",views.invernadero_home,name='home'),
    # url(r'^$', views.obtener_datos, name = "listar"),
    


    
]
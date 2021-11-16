from django.urls import path
from . import views
from django.conf.urls import include, url

urlpatterns = [
    path("agregar/",views.suscripcion_agregar,name='sus_agregar'),
    path("listar/",views.listar_suscribe,name='listar_suscribe'),
    path("filtro_fechas/",views.filtro_fechas,name='filtro_fechas'),
    path("reporte/",views.reportes,name='reporte'),




    path('delete/<path:ruta>/',views.suscribe_delete,name='suscribe_delete'),
    path('<path:ruta>/', views.suscripcion_agregar,name='suscribe_update'), 


]
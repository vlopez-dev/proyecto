from django.urls import path
from . import views

urlpatterns = [
    path("agregar/",views.cliente_agregar,name='cli_agregar'),
    path("listar/",views.listar_cliente,name='listar_cliente'),

    path('<int:id_cliente>/', views.cliente_agregar,name='cliente_update'), # get and post req. for update operation
    path('<int:id_cliente>/', views.cliente_agregar,name='cliente_update'), # get and post req. for update operation

    path('delete/<int:id_cliente>/',views.cliente_delete,name='cliente_delete'),

]
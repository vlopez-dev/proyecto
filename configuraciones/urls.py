from django.urls import path
from . import views


urlpatterns = [
    path("configuraciones/",views.configurciones,name='configuraciones'),


]
from django import forms
from django.db import models
from django.db.models import fields
from .models import Lectura, Suscribe


class SuscribeForm(forms.ModelForm):

    class Meta:
        model = Suscribe
        fields = 'id_cliente','ruta', 'valor_activo', 'actuador'

        labels = {
            'id_cliente':'Conexion','ruta': 'Modelo de Sensor',  'valor_activo': 'Valor para activacion',
            'actuador': 'Encender'


        }

   


class DateInput(forms.DateInput):
    input_type = 'date'


class LecturasForm(forms.ModelForm):
    dia_desde = forms.DateTimeField(required=False)
    dia_hasta = forms.DateTimeField(required=False)

    class Meta:
        model = Lectura
        fields = ['dia_desde', 'dia_hasta']

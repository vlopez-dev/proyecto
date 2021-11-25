from django import forms
from django.db import models
from django.db.models import fields
from .models import Lectura, Suscribe


class SuscribeForm(forms.ModelForm):

    class Meta:
        model = Suscribe
        fields = 'id_cliente','ruta', 'tipo', 'valor_activo', 'actuador', 'valor_actuador'

        labels = {
            'id_cliente':'Cliente','ruta': 'Modelo de Sensor', 'tipo': 'Tipo de sensor', 'valor_activo': 'Valor para activacion',
            'actuador': 'Encender', 'valor_actuador': 'On/Off'


        }

   


class DateInput(forms.DateInput):
    input_type = 'date'


class LecturasForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)
    dia_desde = forms.DateTimeField(required=False)
    dia_hasta = forms.DateTimeField(required=False)

    class Meta:
        model = Lectura
        fields = ['dia_desde', 'dia_hasta']

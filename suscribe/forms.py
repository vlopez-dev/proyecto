from django import forms
from django.db import models
from django.db.models import fields
from .models import  Lectura,Suscribe
from bootstrap_datepicker.widgets import DatePicker

class SuscribeForm(forms.ModelForm):

    class Meta:
        model = Suscribe
        fields = 'ruta','tipo','valor_activo','actuador','valor_actuador'
        
        labels = {
           'ruta':'Ubicacion','tipo':'Tipo de sensor','valor_activo':'Valor para activacion',
           'actuador':'Encender','valor_actuador':'On/Off'
           

        }
        
        

    TIPOSENSOR= [
        ('orange', 'Oranges'),
        ('cantaloupe', 'Cantaloupes'),
        ('mango', 'Mangoes'),
        ('honeydew', 'Honeydews'),
        ]
class DateInput(forms.DateInput):
    input_type = 'date'
class LecturasForm(forms.ModelForm):
	export_to_CSV = forms.BooleanField(required=False)
	dia_desde = forms.DateField(required=False)
	dia_hasta = forms.DateField(required=False)
	class Meta:
		model = Lectura
		fields = ['dia_desde', 'dia_hasta']
        
        date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )
from django import forms
from django.db import models
from django.db.models import fields
from .models import  Lectura,Suscribe

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


        
    # def __init__(self, *args, **kwargs):
    #     super(SuscribeForm, self).__init__(*args, **kwargs)
    #     self.fields['tipo'].empty_label = "Select"
    #     # self.fields['emp_code'].required = False

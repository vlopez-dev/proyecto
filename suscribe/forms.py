from django import forms
from django.db import models
from django.db.models import fields
from .models import  Lectura,Suscribe


class SuscribeForm(forms.ModelForm):

    class Meta:
        model = Suscribe
        fields = '__all__'
        
        
        
# def __init__(self, *args, **kwargs):
#         super(SuscribeForm,self).__init__(*args, **kwargs)
#         self.fields['ruta'].required = False



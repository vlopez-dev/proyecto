from django import forms
from .models import Invernadero
class InvernaderoForm(forms.ModelForm):

    class Meta:
        model = Invernadero
        fields = '__all__'
        
        labels = {
            'Name':'Nombre',
        }
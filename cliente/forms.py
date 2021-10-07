from django import forms
from .models import Cliente
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Invernadero
        fields = '__all__'
        
        labels = {
            'Name':'Nombre',
        }
from django import forms
from .models import Cliente
class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        
        labels = {
            'id_invernadero':'Ubicación',
            'broker_conexion':'Direccion url o ip de conexion',

        }
        
        
def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # self.fields['position'].empty_label = "Select"
        self.fields['broker_conexion'].required = True
        # self.fields['id_invernadero'].required = False

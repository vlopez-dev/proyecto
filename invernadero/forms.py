from django import forms
from .models import Invernadero
class InvernaderoForm(forms.ModelForm):

    class Meta:
        model = Invernadero
        fields = '__all__'
        
        labels = {
            'nombre':'Nombre del lugar',
        }
        
        
        
    # def __init__(self, *args, **kwargs):
    #     super(InvernaderoForm, self).__init__(*args, **kwargs)
    #     # self.fields['position'].empty_label = "Select"
    #     self.fields['nombre'].required = True
    #     # self.fields['id_invernadero'].required = False

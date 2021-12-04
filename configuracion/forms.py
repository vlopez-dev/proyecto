from django import forms
from .models import Configuracion


class ConfiguracionForm(forms.ModelForm):
    passw_from = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={}))

    class Meta:
        model = Configuracion
        fields = 'email_from','passw_from', 'email_to', 'server_config'

        
        labels = {
            'email_from':'Cuenta de mail','passw_from': 'Password',  'email_to': 'Email receptor','server_config':'Configuracion mail'


        }
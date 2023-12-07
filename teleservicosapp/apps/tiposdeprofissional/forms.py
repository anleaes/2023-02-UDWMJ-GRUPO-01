from django import forms
from .models import Tiposdeprofissional

class TiposdeprofissionalForm(forms.ModelForm):

    class Meta:
        model = Tiposdeprofissional
        exclude = ('created_on' , 'updated_on',)
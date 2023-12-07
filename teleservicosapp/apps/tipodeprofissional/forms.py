from django import forms
from .models import Tipodeprofissional

class TipodeprofissionalForm(forms.ModelForm):

    class Meta:
        model = Tipodeprofissional
        exclude = ('created_on' , 'updated_on',)
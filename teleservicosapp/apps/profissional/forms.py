from django import forms
from .models import Profissional

class ProfissionalForm(forms.ModelForm):

    class Meta:
        model = Profissional
        exclude = ('created_on' , 'updated_on',)
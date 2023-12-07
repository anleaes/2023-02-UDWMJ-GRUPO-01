from django import forms
from .models import Profissionais

class ProfissionaisForm(forms.ModelForm):

    class Meta:
        model = Profissionais
        exclude = ('created_on' , 'updated_on',)
        
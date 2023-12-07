from django import forms
from .models import Materiais

class MateriaisForm(forms.ModelForm):

    class Meta:
        model = Materiais
        exclude = ('created_on' , 'updated_on',)
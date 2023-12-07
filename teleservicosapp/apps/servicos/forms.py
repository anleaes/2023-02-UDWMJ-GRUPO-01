from django import forms
from .models import Servicos, Client, ServicosItem, Profissionais

class ServicosForm(forms.ModelForm):
    
    class Meta:
        model = Servicos
        exclude = ('client', 'created_on' , 'updated_on')

class ServicosItemForm(forms.ModelForm):
    
    class Meta:
        model = ServicosItem
        exclude = ('servicos', 'created_on' , 'updated_on')
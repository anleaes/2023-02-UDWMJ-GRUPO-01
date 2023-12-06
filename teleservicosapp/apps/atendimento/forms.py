from django import forms
from .models import Atendimento, Client, Materiais ,MateriaisAtendimento
#import profissional
#import servico

class AtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = Atendimento
        exclude = ('client', 'created_on' , 'updated_on')
        #exclude profissional, servico

class MateriaisAtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = MateriaisAtendimento
        exclude = ('atendimento', 'created_on' , 'updated_on')

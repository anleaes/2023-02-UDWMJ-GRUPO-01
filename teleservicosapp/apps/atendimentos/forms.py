from django import forms
from .models import Atendimentos, Client, Materiais, MateriaisAtendimentos
#import profissional
#import servico

class AtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = Atendimentos
        exclude = ('client', 'created_on' , 'updated_on')
        #exclude profissional, servico

class MateriaisAtendimentoForm(forms.ModelForm):
    
    class Meta:
        model = MateriaisAtendimentos
        exclude = ('atendimentos', 'created_on' , 'updated_on')
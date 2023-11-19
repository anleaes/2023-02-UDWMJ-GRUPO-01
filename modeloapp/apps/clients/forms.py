from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('created_on' , 'updated_on',)

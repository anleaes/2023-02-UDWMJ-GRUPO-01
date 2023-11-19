from django import forms
from .models import Socialnetwork

class SocialnetworkForm(forms.ModelForm):

    class Meta:
        model = Socialnetwork
        exclude = ('created_on' , 'updated_on',)
from django import forms
from .models import *

class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscriber
        exclude = ['']
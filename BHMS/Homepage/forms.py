from django import forms
from .models import Comments,userProfile
from django.contrib.auth.models import User

class Nameform(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','message']


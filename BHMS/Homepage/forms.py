from django import forms
from .models import Comments,userProfile
from django.contrib.auth.models import User


class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','message']

class profileForm(forms.ModelForm):
    class Meta:
        model = userProfile
        fields = ['room_no']


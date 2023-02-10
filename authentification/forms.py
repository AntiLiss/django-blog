from django import forms
from . import models


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=50)
    mail = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=50)
    
    class Meta:
        model = models.User
        fields = '__all__'
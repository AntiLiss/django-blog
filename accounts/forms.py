from django import forms


class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
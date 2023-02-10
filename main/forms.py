from django import forms
from .models import Article


class AddNewForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=False)
    anounce = forms.CharField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Article
        fields = '__all__'
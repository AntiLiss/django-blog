from django import forms
from .models import Article


class AddNewForm(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True, label='titul')
    anounce = forms.CharField(max_length=100, required=True)
    text = forms.CharField(widget=forms.Textarea, required=False)
    
    class Meta:
        model = Article
        fields = '__all__'
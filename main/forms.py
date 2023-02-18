from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):  
    class Meta:
        model = Article
        fields = ['title', 'anounce', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'type title'})
        }
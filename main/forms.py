from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anounce', 'image', 'text']
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'title'}
            ),
            'anounce': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'anonce'}
            ),
            'image': forms.FileInput(
                attrs={'class': 'form-control', 'accept': 'image/*', 'id': 'image'}
            ),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'cols': '30', 'rows': '10', 'id': 'text'}
            ),
        }

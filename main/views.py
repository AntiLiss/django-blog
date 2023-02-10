from django.shortcuts import render, HttpResponse
from . import forms, models

# Create your views here.
def index(request):
    articles = models.Article.objects.order_by('title').reverse()
    # articles = models.Article.objects.raw(raw_query='SELECT * FROM main_article ORDER BY id DESC')
    
    return render(request, template_name='main/news.html', context={'articles': articles})


def add(request):
    if request.method == 'POST':
        article_form = forms.AddNewForm(request.POST)
        if article_form.is_valid():
            article_form.save()
        else:
            return HttpResponse('Invalid data!')
        return render(request, template_name='main/add.html', context={'form': forms.AddNewForm})
    else:
        return render(request, template_name='main/add.html', context={'form': forms.AddNewForm})
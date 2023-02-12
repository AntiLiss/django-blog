from django.shortcuts import render, HttpResponse
from . import forms, models
from django.utils import timezone

# Create your views here.
def index(request):
    articles = models.Article.objects.order_by('id').reverse()
    # articles = models.Article.objects.raw(raw_query='SELECT * FROM main_article ORDER BY id DESC')
    
    return render(request, template_name='main/news.html', context={'articles': articles})


def me(request):
    if request.method == 'POST':
        article_form = forms.AddNewForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author_id = request.user.id
            article.date = timezone.now()
            article.save()
            return render(request, template_name='main/me.html', context={'form': forms.AddNewForm})
        else:
            return render(request, template_name='main/me.html', context={'form': article_form})
    else:
        article_form = forms.AddNewForm()
        return render(request, template_name='main/me.html', context={'form': article_form})
    
from django.shortcuts import render, HttpResponse, redirect
from . import forms, models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import DetailView

# Create your views here.
def index(request):
    articles = models.Article.objects.order_by('date').reverse()
    # articles = models.Article.objects.raw(raw_query='SELECT * FROM main_article ORDER BY id DESC')
    
    return render(request, template_name='main/news.html', context={'articles': articles})


class PostDetailView(DetailView):
    model = models.Article
    template_name = 'main/post_detail.html'


def me(request):
    if request.method == 'POST':
        article_form = forms.AddNewForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author_id = request.user.id
            article.date = timezone.now()
            article.save()
            return redirect('me')
        else:
            articles = models.Article.objects.filter(author_id=int(request.user.id)).order_by('date').reverse()        
            author = User.objects.get(id=request.user.id)
            return render(request, template_name='main/me.html', context={'form': article_form, 'articles': articles, 'author': author})
    else:
        article_form = forms.AddNewForm()
        articles = models.Article.objects.filter(author_id=int(request.user.id)).order_by('date').reverse()        
        author = User.objects.get(id=request.user.id)
        return render(request, template_name='main/me.html', context={'form': article_form, 'articles': articles, 'author': author})
    
from django.shortcuts import render, HttpResponse, redirect
from . import forms, models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView

# Create your views here.

# def index(request):
#     articles = models.Article.objects.order_by('date').reverse()    
#     return render(request, template_name='main/news.html', context={'articles': articles})

class PostsListView(ListView):
    model = models.Article
    ordering = ['author__username']
    # I also can use this raw query below instead two properties above
    # queryset = models.Article.objects.raw(raw_query='SELECT * FROM main_article INNER JOIN auth_user ON main_article.author_id = auth_user.id ORDER BY auth_user.username ASC')
    template_name = 'main/news.html'
    context_object_name = 'articles'


class PostDetailView(DetailView):
    model = models.Article
    template_name = 'main/post_detail.html'


def me(request):
    if request.method == 'POST':
        article_form = forms.AddNewForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.date = timezone.now()
            article.save()
            return redirect('me')
        else:
            articles = models.Article.objects.filter(author=request.user).order_by('date').reverse()        
            return render(request, template_name='main/me.html', context={'form': article_form, 'articles': articles})
    else:
        article_form = forms.AddNewForm()
        articles = models.Article.objects.filter(author=request.user).order_by('date').reverse()        
        return render(request, template_name='main/me.html', context={'form': article_form, 'articles': articles})
    
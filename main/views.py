from django.shortcuts import render, HttpResponse, redirect
from . import forms, models
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# def index(request): 
#     return render(request, template_name='main/profile_detail.html')


class PostListView(ListView):
    model = models.Article
    ordering = ['-date']
    # I also can use the raw query below instead two properties above
    # queryset = models.Article.objects.raw(raw_query='SELECT * FROM main_article INNER JOIN auth_user ON main_article.author_id = auth_user.id ORDER BY auth_user.username ASC')
    template_name = 'main/news.html'
    context_object_name = 'articles'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = models.Article
    template_name = 'main/post_detail.html'
    context_object_name = 'article'
    
    
class AuthorDetailView(DetailView):
    model = User
    template_name = 'main/author_detail.html'
    context_object_name = 'author'


@login_required
def me(request):
    if request.method == 'POST':
        article_form = forms.ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.date = timezone.now()
            article.save()
            return redirect('me')
        else:
            articles = models.Article.objects.filter(author=request.user).order_by('-date')       
            return render(request, template_name='main/my_profile.html', context={'form': article_form, 'articles': articles})
    else:
        article_form = forms.ArticleForm()
        articles = models.Article.objects.filter(author=request.user).order_by('-date')       
        return render(request, template_name='main/my_profile.html', context={'form': article_form, 'articles': articles})
    
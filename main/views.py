from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
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


class PostDetailView(DetailView):
    model = models.Article
    template_name = 'main/post_detail.html'
    context_object_name = 'article'


class AuthorDetailView(DetailView):
    model = User
    template_name = 'main/author_detail.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get all articles posted by this author
        this_user = models.User.objects.get(id=self.kwargs['pk'])
        context['articles'] = models.Article.objects.filter(author=this_user).order_by('-date')
        return context


# @login_required
# def me(request):
#     article_form = forms.ArticleForm()
#     articles = request.user.article_set.order_by('-date')
#     # I also could do it like this
#     # articles = models.Article.objects.filter(author=request.user).order_by('-date')
#     return render(request, template_name='main/my_profile.html', context={'article_form': article_form, 'articles': articles})


# class based view version for url `me`
class MyPostListView(LoginRequiredMixin, ListView):
    template_name = 'main/my_profile.html'
    # context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        queryset = self.request.user.article_set.order_by('-date')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_form'] = forms.ArticleForm()
        return context


@login_required
def create_article(request):
    if request.method == 'POST':
        article_form = forms.ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.author = request.user
            article.save()
            article_block = render(request, 'main/article_block.html', context={'article': article}).content.decode('utf-8')
            return JsonResponse({'success': True, 'article_block': article_block})
        else:
            return JsonResponse({'errors': article_form.errors})


# I should to add AJAX in this view
@login_required
def update_article(request, pk):
    if request.method == 'POST':
        article = models.Article.objects.get(id=pk)
        form = forms.ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('me')
        else:
            return HttpResponse('<h1>Not valid form data!</h1>')
    else:
        return HttpResponse('<h1>Not a POST method!</h1>')


# Problem: if I delete DetailView entry then I get error: No such page
@login_required
def delete_article(request, pk):
    models.Article.objects.filter(id=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))

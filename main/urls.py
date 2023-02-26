from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.PostListView.as_view(), name='news'),
    path('', views.PostListView.as_view(), name='news'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('me', views.me, name='me'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('update_article/<int:pk>', views.update_article, name='update_article')
]
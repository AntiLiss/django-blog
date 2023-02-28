from django.urls import path, include
from . import views


urlpatterns = [
    # path('', views.PostListView.as_view(), name='news'),
    path('', views.PostListView.as_view(), name='news'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('me', views.MyPostListView.as_view(), name='me'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author_detail'),
    path('create-article', views.create_article, name='create-article'),
    path('update_article/<int:pk>', views.update_article, name='update_article'),
    path('delete-article/<int:pk>', views.delete_article, name='delete-article')
]
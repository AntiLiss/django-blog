from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='news'),
    path('<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('me', views.me, name='me'),

]
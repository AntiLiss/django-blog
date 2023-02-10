from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='news'),
    path('add', views.add, name='add')

]
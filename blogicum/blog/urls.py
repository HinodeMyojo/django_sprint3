"""Calls the function corresponding to the query.

For example, if we have a request for the path <domain>/posts/1
The urlpatterns variable will start the 'post_detail' function,
which is located in the 'views' file, assign name=post_detail to it.
"""
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('category/<slug:category_slug>/', views.category_posts,
         name='category_posts')
]

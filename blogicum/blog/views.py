"""Page content display functions file."""

from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
from django.utils import timezone

def index(request):
    """Returns file index.html with reversed dictionary."""
    template = 'blog/index.html'

    post_list = Post.objects.values(
        'id', 'title', 'pub_date', 'author',
        'location', 'category'
        ).filter(is_published=True, pub_date__lte=timezone.now())[:5]
    
    context = {'post_list': post_list}

    return render(request, template, context)


def post_detail(request, id):
    """Returns a specific page, according to the <id> query."""
    template = 'blog/detail.html'

    post = Post.objects.values(
        'id', 'title', 'pub_date', 'author',
        'location', 'category'
    ).filter(is_published=True, pub_date__lte=timezone.now(), id=id)

    context = {
        'post': post
    }

    return render(request, template, context)


def category_posts(request, category_slug):
    """Returns a specific page, according to the <category> query."""
    template = 'blog/category.html'

    category = get_object_or_404(Post.objects.values('id', 'title').filter(is_published=True, slug=category_slug))

    context = {
        'category': category
    }

    return render(request, template, context)

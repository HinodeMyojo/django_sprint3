"""Page content display functions file."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from .models import Post, Category
from django.utils import timezone
from django.db.models import Q


def index(request: HttpRequest) -> HttpResponse:
    """View function for rendering the index page of the blog."""
    # Set the template for the page
    template = 'blog/index.html'

    # Get the latest 5 published posts with their related categories
    post_list = Post.objects.filter(
        Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
        & Q(category__is_published=True)
    ).select_related('category').order_by('-pub_date')[:5]

    # Create a dictionary to pass the post list to the template
    context = {'post_list': post_list}

    # Render the template with the context data and return the response
    return render(request, template, context)


def post_detail(request: HttpRequest, id: int) -> HttpResponse:
    """
    Returns the detail page of a specific post identified by the given id.

    Args:
        request (HttpRequest): The HTTP request object.
        id (int): The id of the post to retrieve.

    Returns:
        HttpResponse: The HTTP response containing the rendered detail page.
    """
    # Define the template for the detail page
    template = 'blog/detail.html'

    # Retrieve the post from the database using the id
    post = get_object_or_404(
        Post.objects.filter(
            Q(is_published=True)
            & Q(pub_date__lte=timezone.now())
            & Q(category__is_published=True)
        ),
        id=id
    )

    # Define the context data to be passed to the template
    context = {
        'post': post
    }

    # Render the detail page with the given context data
    return render(request, template, context)


def category_posts(request: HttpRequest, category_slug: str) -> HttpResponse:
    """Returns a specific page, according to the <category> query."""
    # Define the template for the category page
    template = 'blog/category.html'

    # Retrieve the categpry from database
    category = get_object_or_404(
        Category.objects,
        slug=category_slug,
        is_published=True)
    post_list = Post.objects.filter(
        Q(category=category)
        & Q(is_published=True)
        & Q(pub_date__lte=timezone.now())
    ).order_by('-created_at')

    # Define the context data to be passed to the template
    context = {
        'category': category,
        'post_list': post_list
    }

    # Render the category page with the given context data
    return render(request, template, context)

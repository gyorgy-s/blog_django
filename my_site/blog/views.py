from django.shortcuts import render

from datetime import date

from .models import Post


def home(request):
    latest_posts = Post.objects.order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    sorted_posts = Post.objects.order_by("-date")
    return render(request, "blog/posts.html", {
        "posts": sorted_posts,
    })


def post_detail(request, slug):
    post_to_display = Post.objects.get(slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": post_to_display,
    })

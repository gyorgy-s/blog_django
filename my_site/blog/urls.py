from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("posts", view=views.posts, name="posts"),
    path("posts/<slug:slug>", view=views.post_detail, name="post-detail"),  # /posts/my-first-post
]

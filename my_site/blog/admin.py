from django.contrib import admin

from .models import Author, Tag, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["caption", "color"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "author"]
    prepopulated_fields = {"slug": ["title"][:50]}

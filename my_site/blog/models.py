from django.db import models
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20, null=False, blank=False, default=None)
    color = models.CharField(max_length=9, null=False, default="#93d7b7db")

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150, null=False, blank=False)
    excerpt = models.CharField(max_length=255, null=False, blank=False)
    image_name = models.CharField(max_length=100, null=False, blank=True, default="leaf.jpg")
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)
    slug = models.SlugField(null=False, blank=True, db_index=True, unique=True)

    author = models.ForeignKey(
        Author, default=0, on_delete=models.SET_DEFAULT, related_name="posts"
    )

    tags = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title)
        if kwargs.get("update_fields") and "title" in kwargs.get("update_fields"):
            kwargs["update_fields"] = {"slug"}.union(kwargs["update_fields"])
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title[:30]}"

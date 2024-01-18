from django.shortcuts import render

from datetime import date

# Create your views here.

post_data = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Maximilian",
        "date": date(2024, 1, 16),
        "title": "Mountain Hiking",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur iusto quam placeat \
            exercitationem accusantium! Similique illo alias dolores perspiciatis nesciunt nobis laborum qui quam, \
                reiciendis necessitatibus sapiente at animi aspernatur.",
        "content": """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cumque eum minima eveniet! Ipsa mollitia vel
            laboriosam repellat alias, distinctio doloribus facere voluptatum nulla? Odit, itaque odio. Est, minima
            nihil quia consectetur quibusdam quis, animi iste repellendus odio doloribus libero alias at sit odit vero
            omnis! Cumque obcaecati magnam.
        """,
    },
    {
        "slug": "a-very-fine-leaf",
        "image": "leaf.jpg",
        "author": "Tina",
        "date": date(2024, 1, 17),
        "title": "A Very Fine Leaf",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur iusto quam placeat \
            exercitationem accusantium! Similique illo alias dolores perspiciatis nesciunt nobis laborum qui quam, \
                reiciendis necessitatibus sapiente at animi aspernatur.",
        "content": """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cumque eum minima eveniet! Ipsa mollitia vel
            laboriosam repellat alias, distinctio doloribus facere voluptatum nulla? Odit, itaque odio. Est, minima
            nihil quia consectetur quibusdam quis, animi iste repellendus odio doloribus libero alias at sit odit vero
            omnis! Cumque obcaecati magnam.
        """,
    },
    {
        "slug": "lanterns-on-the-streat",
        "image": "lanterns.jpg",
        "author": "Yui",
        "date": date(2024, 1, 17),
        "title": "Lanterns On The Streat",
        "excerpt": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur iusto quam placeat \
            exercitationem accusantium! Similique illo alias dolores perspiciatis nesciunt nobis laborum qui quam, \
                reiciendis necessitatibus sapiente at animi aspernatur.",
        "content": """
            Lorem, ipsum dolor sit amet consectetur adipisicing elit. Cumque eum minima eveniet! Ipsa mollitia vel
            laboriosam repellat alias, distinctio doloribus facere voluptatum nulla? Odit, itaque odio. Est, minima
            nihil quia consectetur quibusdam quis, animi iste repellendus odio doloribus libero alias at sit odit vero
            omnis! Cumque obcaecati magnam.
        """,
    },
]


def get_date(post):
    return post["date"]


def home(request):
    sorted_posts = sorted(post_data, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts,
    })


def posts(request):
    sorted_posts = sorted(post_data, key=get_date, reverse=True)
    return render(request, "blog/posts.html", {
        "posts": sorted_posts,
    })


def post_detail(request, slug):
    post_to_display = next(post for post in post_data if post["slug"] == slug)
    return render(request, "blog/post-detail.html", {
        "post": post_to_display,
    })

from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def posts(request):
    pass


def post(request):
    pass

from django.shortcuts import render
from django.http import HttpResponse


posts= [
    {
        'author': 'Abdullah',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2023'
    },
     {
        'author': 'Monir',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2023'
    },
     {
        'author': 'Nasir',
        'title': 'Blog Post 3',
        'content': 'Third post content',
        'date_posted': 'August 27, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')



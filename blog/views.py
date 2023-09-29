from django.shortcuts import render

posts = [
    {
        'author': 'fname1 lname1',
        'title': 'Blog Post 1',
        'content': 'First Content',
        'date_posted': 'Sept 29, 2023'
    },
    {
        'author': 'fname2 lname2',
        'title': 'Blog Post 2',
        'content': 'Second Content',
        'date_posted': 'Sept 29, 2023'
    }
]


def home(request):
    context = {
        'posts': posts,
        'title': 'Blog-Home',
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')


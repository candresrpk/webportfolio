from django.shortcuts import render

# Create your views here.


def blogView(request):
    context = {
        'title': 'Blog'
    }
    return render(request, 'blog/home.html', context)
from django.shortcuts import render


def hossaikView(request):
    context = {
        'title': 'Hossaik'
    }
    return render(request, 'hossaik/index.html', context)
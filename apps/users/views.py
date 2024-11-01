from django.shortcuts import render

# Create your views here.


def loginView(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'users/login.html', context)
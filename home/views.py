from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'title': 'home',
    }
    return render(request, 'home/home.html', context)

def error_404(request, exception):
        data = {}
        return render(request, 'home/errors/404.html', data)

def error_403(request, exception):
        data = {}
        return render(request, 'home/errors/403.html', data)

def error_400(request, exception):
        data = {}
        return render(request, 'home/errors/400.html', data)

def error_500(request,  exception):
        data = {}
        return render(request, 'home/errors/500.html', data)

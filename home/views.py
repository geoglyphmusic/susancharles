from django.shortcuts import render
from django.http import HttpResponse
from .models import Homepage
from articles.models import Article

def home(request):
    context = {
        'title': 'home',
        'homepage_list': Homepage.objects.filter(active=True),
        'article_list': Article.objects.order_by("-date_published")[:3]
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

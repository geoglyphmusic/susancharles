from django.shortcuts import render
from django.http import HttpResponse
from .models import Homepage
from articles.models import Article
from people.models import Person

def home(request):
    context = {
        'title': 'home',
        'homepage_list': Homepage.objects.filter(active=True),
        'article_list': Article.objects.order_by("-date_published")[:3],
        'person_list': Person.objects.order_by("-date_published")[:3]
    }
    return render(request, 'home/home.html', context)

def error_404(request, exception):
    return render(request, 'home/errors/404.html', status=404)

def error_500(request):
    return render(request, 'home/errors/500.html', status=500)

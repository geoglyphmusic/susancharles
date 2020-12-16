from django.shortcuts import render, get_object_or_404
from .models import Article
from taggit.models import Tag

def articles_main_view(request):
	context = {
		'articles': Article.objects.all(),
		'tags': Tag.objects.all()
	}
	return render(request, 'articles/articles_main.html', context)

def article_view(request, article_slug):
    context = {
        'article': get_object_or_404(Article, slug=article_slug)
    }
    return render(request, 'articles/article.html', context)

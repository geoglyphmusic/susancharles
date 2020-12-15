from django.shortcuts import render, get_object_or_404
from .models import Article
from taggit.models import Tag


def articles_main_view(request):
	context = {
		'articles': Article.objects.all(),
		'tags': Article.tags.most_common()
	}
	return render(request, 'articles/articles_main.html', context)

def article_view(request, article_slug):
    context = {
        'article': get_object_or_404(Article, slug=article_slug)
    }
    return render(request, 'articles/article.html', context)

def tag_view(request, selected_tag):
    context = {
        'selected_tag': selected_tag,
		'tags': Article.tags.most_common(),
        'articles': Article.objects.filter(tags__name__in=[selected_tag])
    }
    return render(request, 'articles/articles_main.html', context)

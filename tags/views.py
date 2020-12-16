from django.shortcuts import render, get_object_or_404
from taggit.models import Tag
from articles.models import Article
from people.models import Person
from collections import OrderedDict


# Create your views here.
def tag_view(request, selected_tag):
    selected_tag = get_object_or_404(Tag, name=selected_tag)
    article_list = Article.objects.filter(tags__name__in=[selected_tag])
    person_list = Person.objects.filter(tags__name__in=[selected_tag])
    combined_list = set(list(article_list) + list(person_list))
    context = {
        'selected_tag': selected_tag,
        'tags': Tag.objects.all(),
        'article_list': article_list,
        'person_list': person_list,
        'combined_list': combined_list
    }
    return render(request, 'tags/tag.html', context)

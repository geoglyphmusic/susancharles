from django.shortcuts import render, get_object_or_404
from .models import Person
from taggit.models import Tag

def people_main(request):
    context = {
        'people': Person.objects.all(),
        'tags': Person.tags.most_common()
    }
    return render(request, 'people/people_main.html', context)


def person_view(request, person_slug):
    context = {
        'person': get_object_or_404(Person, slug=person_slug)
    }
    return render(request, 'people/person.html', context)

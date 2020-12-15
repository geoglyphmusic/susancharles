from django.urls import path

from . import views

urlpatterns = [
    path('', views.people_main, name='people'),
    path('<person_slug>', views.person_view, name='person'),
]

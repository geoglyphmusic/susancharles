from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles_main_view, name='articles'),
    path('<article_slug>', views.article_view, name='article'),
    path('tag/<selected_tag>', views.tag_view, name='tag')
]

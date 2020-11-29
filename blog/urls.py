from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('post/<post_slug>', views.post_view, name='post'),
    path('tag/<tag_slug>', views.post_view, name='post')
]

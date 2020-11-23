from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('post/<post_slug>', views.post, name='post')
]

from django.urls import path

from . import views

urlpatterns = [
    path('<selected_tag>', views.tag_view, name='tag'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.services_main_view, name='services'),
]

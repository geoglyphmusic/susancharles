"""susancharles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500

from home import views as home_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('articles/', include('articles.urls')),
    path('people/', include('people.urls')),
    path('tag/', include('tags.urls')),
    path('services/', include('services.urls')),
    path('user/', include('user.urls')),
    path('contact/', include('contact.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = home_views.error_404
handler500 = home_views.error_500

admin.site.site_header = 'Corrichie Ancestry'
admin.site.site_title = 'Corrichie Ancestry'
admin.site.index_title = "Welcome to the Corrichie Ancestry admin page."

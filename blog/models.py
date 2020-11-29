import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from taggit.managers import TaggableManager


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    date_published = models.DateTimeField('date published', null=True)
    tags = TaggableManager()


    def __str__(self):
        return self.title

    class Meta:
    	ordering = ['-date_published']

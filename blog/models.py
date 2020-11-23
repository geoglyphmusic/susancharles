import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    slug = AutoSlugField(populate_from='title')
    date_published = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.title

    class Meta:
    	ordering = ['-date_published']

import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    content = RichTextUploadingField(blank=True, null=True)
    # content = models.TextField()
    date_published = models.DateTimeField('date published', null=True)
    tags = TaggableManager()


    def __str__(self):
        return self.title

    class Meta:
    	ordering = ['-date_published']

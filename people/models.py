import datetime
from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Person(models.Model):
    name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    year_of_death = models.IntegerField()
    slug = AutoSlugField(populate_from='name')
    abstract = models.TextField()
    content = RichTextUploadingField(blank=True, null=True)
    date_published = models.DateTimeField('date published', null=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    class Meta:
    	ordering = ['-date_published']

from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField



# Create your models here.

class Blog(models.Model):
    #title = models.CharField(max_length=200, blank=True, null=True )
    #body1 = models.TextField(blank=True, null=True)
    #body2 = models.TextField(blank=True, null=True)
    #body3 = models.TextField(blank=True, null=True)
    #body4 = models.TextField(blank=True, null=True)
    #created_at = models.DateTimeField(default=datetime.now, blank=True)

    title = RichTextField(blank=True, null=True)
    body1 = RichTextField(blank=True, null=True)
    body2 = RichTextField(blank=True, null=True)
    body3 = RichTextField(blank=True, null=True)
    body4 = RichTextField(blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    #title = models.CharField(max_length=200)
    #body1 = models.TextField()
    #body2 = models.TextField()
    #body3 = models.TextField()
    #body4 = models.TextField()
    #created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
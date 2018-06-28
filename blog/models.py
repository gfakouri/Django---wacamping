from django.db import models
from datetime import datetime



# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body1 = models.TextField()
    body2 = models.TextField()
    body3 = models.TextField()
    body4 = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone

# Create your models here.
class PostItem(models.Model):
    post_title = models.CharField(max_length=30)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(default=timezone.now)
    results = models.IntegerField(default=0)
    #boast = models.BooleanField(default=False)

    def __str__(self):
        return self.post_title



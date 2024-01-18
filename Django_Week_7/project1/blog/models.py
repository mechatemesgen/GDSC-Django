from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):

    class CurrentStatus(models.TextChoices):
        PUBLISHED ='pu', 'Published'
        DRAFT = 'dr', 'Draft'

    title = models.CharField(max_length=100)
    content = models.TextField()
    # author = 


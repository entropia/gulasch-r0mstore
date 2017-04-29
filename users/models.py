from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    github = models.CharField('github', max_length=128, blank=True)
    twitter = models.CharField('twitter', max_length=128, blank=True)

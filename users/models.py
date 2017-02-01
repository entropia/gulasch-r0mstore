from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    github = models.CharField('github handle', max_length=128)

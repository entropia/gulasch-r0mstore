from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

twitter_validator = RegexValidator(regex=r'^[a-zA-Z0-9_]+$', message='Bitte nur den Benutzername, ohne führendes @.')
github_validator = RegexValidator(regex=r'^[a-z\d](?:[a-z\d]|-(?=[a-z\d]))*$', message='Bitte nur den Benutzername, nicht die Profil-Url.')

class User(AbstractUser):
    github = models.CharField('Github Benutzername', max_length=38, blank=True, validators=[github_validator])
    twitter = models.CharField('Twitter Benutzername', max_length=15, blank=True, validators=[twitter_validator])

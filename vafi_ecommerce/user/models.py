from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    limit = models.IntegerField(default=3)
    onuse = models.IntegerField(default=0)
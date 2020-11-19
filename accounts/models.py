from django.db import models
from django.contrib.auth.models import AbstractUser


class User (AbstractUser):
    promo_code = models.CharField(max_length=200)
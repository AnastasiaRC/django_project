from django.db import models
from django.contrib.auth.models import AbstractUser
from catalog.models import NULLABLE


class User(AbstractUser):
    avatar = models.ImageField(upload_to='media/users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name='телефон',**NULLABLE)
    country = models.CharField(max_length=30, verbose_name='страна', **NULLABLE)
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
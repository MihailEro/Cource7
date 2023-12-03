from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.PositiveIntegerField(unique=True, verbose_name='tg id', blank=True, null=True)
    telegram_username = models.CharField(unique=True, verbose_name='telegram username', max_length=255, null=True,
                                         blank=True)

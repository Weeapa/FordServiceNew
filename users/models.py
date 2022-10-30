from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class Role(models.TextChoices):
    """Роли пользователей"""

    CUSTOMER = 'CUSTOMER', 'клиент'
    WORKER = 'WORKER', 'слесарь'
    MANAGER = 'MANAGER', 'управляющий'
    MASTER = 'MASTER', 'мастер'


class User(AbstractUser):
    email = models.EmailField(
        _("email address"),
        unique=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta():
        verbose_name = "пользователь"

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser):
    email = models.EmailField(_('email address'), unique=True)
    # image = models.ImageField(_('Image'), max_length=500)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username']

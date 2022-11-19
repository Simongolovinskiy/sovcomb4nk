from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib import admin


class User(AbstractUser, PermissionsMixin, models.Model ):
    pass




from django.contrib.auth.models import AbstractUser
from django.db import models
from django_utils.models import UUIDTimeStampModel


class User(UUIDTimeStampModel, AbstractUser):
    birthdate = models.DateField(verbose_name='birthdate', null='True')

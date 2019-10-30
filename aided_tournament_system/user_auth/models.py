from django.contrib.auth.models import AbstractUser
from django.db import models
from django_utils.models import UUIDTimeStampModel


class User(UUIDTimeStampModel, AbstractUser):
    birthdate = models.DateField(verbose_name='birthdate',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} *{self.username}*'

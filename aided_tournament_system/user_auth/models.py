from django.contrib.auth.models import AbstractUser
from django.db import models
from django_countries.fields import CountryField
from django_utils.models import UUIDTimeStampModel

from .choices import GenderChoices


class User(UUIDTimeStampModel, AbstractUser):
    gender = models.CharField(max_length=1,
                              choices=GenderChoices.get_choices(),
                              verbose_name='gender',
                              null=True,
                              blank=True)
    country = CountryField(blank_label='(select country)',
                           verbose_name='country',
                           null=True,
                           blank=True)
    birthdate = models.DateField(verbose_name='birthdate',
                                 null=True,
                                 blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} *{self.username}*'

from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
from user_auth.models import User
from enum import Enum
import uuid as uuid_lib


class Player(User):
    class SEXES(Enum):
        woman = ('w', 'Woman')
        man = ('m', 'Man')

    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    slug = models.SlugField(unique=True)
    sex = models.CharField(
        max_length=1,
        choices=[x.value for x in SEXES]
    )

    country = CountryField(
        blank_label='(select country)'
    )
    rating = models.IntegerField(
        null=True
    )

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})


class Team(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    slug = models.SlugField(unique=True)
    title = models.CharField(
        max_length=100
    )
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        null=True
    )

    def get_absolute_url(self):
        return reverse('flavors:detail', kwargs={'slug': self.slug})

from django.db.models import Manager


class GameManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("competition")

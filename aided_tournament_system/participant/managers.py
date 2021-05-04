from django.db.models import Manager


class PlayerManager(Manager):
    def get_queryset(self):
        return super().get_queryset().prefetch_related("team")

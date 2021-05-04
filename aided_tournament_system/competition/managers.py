from django.db.models import Manager


class RankingsManager(Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("competition", "team")

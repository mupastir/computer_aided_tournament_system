from django.db import models
from participant.models import Team
import uuid as uuid_lib


class Game(models.Model):
    uuid = models.UUIDField(
        db_index=True,
        default=uuid_lib.uuid4,
        editable=False
    )
    team_1 = models.OneToOneField(Team, on_delete=models.PROTECT)
    score_team_1 = models.IntegerField(null=False)
    score_team_2 = models.IntegerField(null=False)

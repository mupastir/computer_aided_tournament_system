from django.db import models
from django_utils.models import UUIDTimeStampModel
from participant.models import Team

from .choices import ScheduleChoices
from .managers import RankingsManager


class Application(UUIDTimeStampModel):
    team = models.ForeignKey(Team,
                             verbose_name='Team',
                             on_delete=models.SET_NULL,
                             related_name='applications',
                             null=True)
    competition = models.ForeignKey('Competition',
                                    on_delete=models.CASCADE,
                                    verbose_name='competition',
                                    related_name='applications')
    is_open = models.BooleanField(default=True,
                                  verbose_name='Is application open')

    def __str__(self):
        return f'{self.competition.title}: {self.team.title}'

    class Meta:
        db_table = 'applications'
        unique_together = ('team', 'competition')


class Ranking(UUIDTimeStampModel):
    place = models.IntegerField(verbose_name='place')
    team = models.ForeignKey(Team,
                             on_delete=models.SET_NULL,
                             verbose_name='Team',
                             related_name='rankings',
                             null=True)
    competition = models.ForeignKey('Competition',
                                    on_delete=models.CASCADE,
                                    verbose_name='competition')
    ranking = models.IntegerField(verbose_name='ranking points')
    objects = RankingsManager()

    def __str__(self):
        return f'{self.competition.title}: {self.team.title}'

    class Meta:
        db_table = 'rankings'
        unique_together = ('competition', 'team')


class Competition(UUIDTimeStampModel):
    title = models.CharField(max_length=300,
                             verbose_name='title')
    start_time = models.DateTimeField(verbose_name='start time')
    end_time = models.DateTimeField(verbose_name='end time')
    courts_number = models.IntegerField(verbose_name='courts number')
    schedule_system = models.CharField(choices=ScheduleChoices.get_choices(),
                                       max_length=2,
                                       verbose_name='Schedule by number '
                                                    'of teams participated')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'competition'

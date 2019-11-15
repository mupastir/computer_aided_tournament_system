from competition.choices import CompetitionTypeChoices
from django.db import models
from django_utils.models import UUIDTimeStampModel
from participant.models import Team

from .choices import GenderChoices, ScheduleChoices
from .managers import RankingsManager


class Application(UUIDTimeStampModel):
    team = models.ForeignKey(Team,
                             verbose_name='Team',
                             on_delete=models.CASCADE,
                             related_name='applications',
                             null=True)
    competition = models.ForeignKey('Competition',
                                    on_delete=models.CASCADE,
                                    verbose_name='competition',
                                    related_name='applications')
    objects = RankingsManager()

    def __str__(self):
        return f'{self.competition.title}: {self.team.title}'

    class Meta:
        db_table = 'applications'
        unique_together = ('team', 'competition')


class Ranking(UUIDTimeStampModel):
    place = models.IntegerField(verbose_name='place', null=True)
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
        return f'{self.team.title}. place {self.place}. ' \
               f'comp: {self.competition.title}'

    class Meta:
        db_table = 'rankings'
        unique_together = ('competition', 'team')


class Competition(UUIDTimeStampModel):
    title = models.CharField(max_length=300,
                             verbose_name='title',
                             unique=True)
    is_open = models.BooleanField(default=True,
                                  verbose_name='are applications open')
    start_time = models.DateTimeField(verbose_name='start time')
    end_time = models.DateTimeField(verbose_name='end time')
    courts_number = models.IntegerField(verbose_name='courts number')
    schedule_system = models.CharField(
        choices=ScheduleChoices.get_choices(),
        max_length=2,
        default=ScheduleChoices.TEAM_SYSTEM_OF_16.value,
        verbose_name='Schedule by number '
                     'of teams participated'
    )
    type = models.CharField(choices=CompetitionTypeChoices.get_choices(),
                            max_length=40,
                            default=CompetitionTypeChoices.PARK_VOLLEY.value,
                            verbose_name='Type of competition')
    gender = models.CharField(choices=GenderChoices.get_choices(),
                              max_length=1,
                              default=GenderChoices.MAN.value,
                              verbose_name='gender')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'competition'

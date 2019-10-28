import datetime

from django.db import models


class Application(models.Model):
    competition = models.ForeignKey('Competition',
                                    on_delete=models.PROTECT,
                                    verbose_name='competition')

    @property
    def is_open(self):
        return (Competition.start_time.to_python(Competition.start_time)
                - datetime.datetime.now()).days <= 2


class Ranking(models.Model):
    competition = models.ForeignKey('Competition',
                                    on_delete=models.CASCADE,
                                    verbose_name='competition')
    ranking = models.IntegerField()


class Competition(models.Model):
    title = models.CharField(max_length=300,
                             verbose_name='title')
    start_time = models.DateTimeField(verbose_name='start time')
    end_time = models.DateTimeField(verbose_name='end time')
    courts_number = models.IntegerField()

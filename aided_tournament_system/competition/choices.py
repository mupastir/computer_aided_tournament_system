from django_utils.choices import BaseChoices


class ScheduleChoices(BaseChoices):
    TEAM_SYSTEM_OF_16 = ('16', '16 Teams system')
    TEAM_SYSTEM_OF_32 = ('32', '32 Team system')

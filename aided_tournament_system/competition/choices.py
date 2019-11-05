from django_utils.choices import BaseChoices, StrChoice


class ScheduleChoices(BaseChoices):
    TEAM_SYSTEM_OF_16 = StrChoice('16', '16 Teams system')
    TEAM_SYSTEM_OF_32 = StrChoice('32', '32 Team system')


class GenderChoices(BaseChoices):
    woman = StrChoice('w', 'Woman')
    man = StrChoice('m', 'Man')

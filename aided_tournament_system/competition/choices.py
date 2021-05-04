from django_utils.choices import BaseChoices, StrChoice


class ScheduleChoices(BaseChoices):
    TEAM_SYSTEM_OF_8 = StrChoice("8", "8 Teams system")
    TEAM_SYSTEM_OF_16 = StrChoice("16", "16 Teams system")
    TEAM_SYSTEM_OF_32 = StrChoice("32", "32 Team system")


class CompetitionTypeChoices(BaseChoices):
    BEACH_VOLLEY = StrChoice("Beach", "Beach Volleyball")
    PARK_VOLLEY = StrChoice("4X4", "4X4 Volleyball")


class GenderChoices(BaseChoices):
    WOMAN = StrChoice("w", "Woman")
    MAN = StrChoice("m", "Man")
    MIXES = StrChoice("x", "Mixes")

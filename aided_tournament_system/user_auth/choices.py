from django_utils.choices import BaseChoices, StrChoice


class GenderChoices(BaseChoices):
    woman = StrChoice("w", "Woman")
    man = StrChoice("m", "Man")

from django_utils.choices import BaseChoices, StrChoice


class RefereeRoles(BaseChoices):
    first = StrChoice('1st', 'First')
    second = StrChoice('2nd', 'Second')
    scorer = StrChoice('scr', 'Scorer')
    line_judge = StrChoice('lnj', 'Line judge')

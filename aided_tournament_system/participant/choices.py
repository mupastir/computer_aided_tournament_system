from django_utils.choices import BaseChoices


class GenderChoices(BaseChoices):
    woman = ('w', 'Woman')
    man = ('m', 'Man')

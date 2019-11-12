from competition.choices import CompetitionTypeChoices, GenderChoices
from django import forms


class RatingChoiceForm(forms.Form):
    type = forms.ChoiceField(choices=CompetitionTypeChoices.get_choices())
    gender = forms.ChoiceField(choices=GenderChoices.get_choices())

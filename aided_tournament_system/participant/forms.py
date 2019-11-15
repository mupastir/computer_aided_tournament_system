from competition.choices import CompetitionTypeChoices, GenderChoices
from django import forms


class RatingChoiceForm(forms.Form):
    type = forms.ChoiceField(choices=CompetitionTypeChoices.get_choices(),
                             label="Тип")
    gender = forms.ChoiceField(choices=GenderChoices.get_choices(),
                               label="Пол")

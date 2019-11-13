from competition.models import Competition, Application
from django import forms

from participant.models import Team


class CompetitionChoiceForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['type']


class ApplicationAddForm(forms.Form):
    team = forms.ModelChoiceField(queryset=Team.objects.all())


class CompetitionCreateForm(forms.ModelForm):

    class Meta:
        model = Competition
        fields = ['title',
                  'start_time',
                  'end_time',
                  'courts_number',
                  'schedule_system',
                  'type',
                  'gender']

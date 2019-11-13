from competition.models import Competition
from django import forms


class CompetitionChoiceForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['type']


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

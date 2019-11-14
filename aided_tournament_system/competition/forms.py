from competition.models import Competition
from django import forms
from participant.models import Player, Team


class CompetitionChoiceForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['type']


class ApplicationAddForm(forms.ModelForm):
    player = forms.ModelMultipleChoiceField(queryset=Player.objects.all())

    class Meta:
        model = Team
        fields = ['title']

    def clean_player(self):
        player = self.cleaned_data['player']
        if not player:
            raise forms.ValidationError("Not enough players in a team")

        if len(player) > 6:
            raise forms.ValidationError("Too many players in a team")

        return player


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

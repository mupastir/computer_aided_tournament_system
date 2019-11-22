from django_select2.forms import Select2MultipleWidget

from competition.models import Competition
from django import forms
from django.forms import DateTimeInput
from django.utils.translation import gettext_lazy as _
from participant.models import Player, Team


class CompetitionChoiceForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['type']
        labels = {'type': _('Тип')}


class ApplicationAddForm(forms.ModelForm):
    player = forms.ModelMultipleChoiceField(queryset=Player.objects.all(),
                                            widget=Select2MultipleWidget,
                                            label="Игроки")

    class Meta:
        model = Team
        fields = ['title']
        labels = {'title': _('Название')}

    def clean_player(self):
        player = self.cleaned_data['player']
        if not player:
            raise forms.ValidationError("Not enough players in a team")

        if len(player) > 6:
            raise forms.ValidationError("Too many players in a team")

        return player


class CompetitionCreateForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=DateTimeInput(
        attrs={'type': 'datetime-local'}
    ), input_formats=['%Y-%m-%dT%H:%M'])
    end_time = forms.DateTimeField(widget=DateTimeInput(
        attrs={'type': 'datetime-local'}
    ), input_formats=['%Y-%m-%dT%H:%M'])

    class Meta:
        model = Competition
        fields = ['title',
                  'start_time',
                  'end_time',
                  'courts_number',
                  'schedule_system',
                  'type',
                  'gender']
        labels = {'title': _('Название'),
                  'start_time': _('Время начала'),
                  'end_time': _('Время окончания'),
                  'courts_number': _('Количество кортов'),
                  'schedule_system': _('Количество команд'),
                  'type': _('Тип'),
                  'gender': _('Пол')}

from datetime import timedelta
from uuid import UUID

from competition.choices import GenderChoices
from competition.constants import HOURS_TO_CLOSE_APPLICATIONS
from competition.forms import (ApplicationAddForm, CompetitionChoiceForm,
                               CompetitionCreateForm)
from competition.tasks import (application_closing_task,
                               calculate_team_rating_task,
                               ranking_creation_task, schedule_creating_task,
                               seeding_teams_task)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView, TemplateView
from participant.models import Player, Team
from participant.tasks import recalculate_rating_task

from .models import Application, Competition


class CompetitionChoiceView(FormView):
    template_name = "competitions_list.html"
    form_class = CompetitionChoiceForm

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        self.success_url = reverse_lazy('competition_filtered',
                                        kwargs={
                                            'competition_type':
                                                form.data['type'],
                                            'competition_gender':
                                                form.data['gender']
                                        })
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['competitions'] = Competition.objects.all().order_by(
            '-start_time'
        )
        return super().get_context_data(**kwargs)


class CompetitionFilteredView(CompetitionChoiceView):

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['competitions'] = Competition.objects.filter(
            type=self.kwargs['competition_type'],
            gender=self.kwargs['competition_gender']
        ).order_by('-created')
        return kwargs


class CompetitionCreateView(CreateView):
    template_name = "competition_create_form.html"
    form_class = CompetitionCreateForm

    def get_success_url(self):
        (application_closing_task.si(self.object.id) |
         ranking_creation_task.si(self.object.id) |
         schedule_creating_task.si(self.object.id,
                                   self.object.schedule_system) |
         seeding_teams_task.si(self.object.id)
         ).apply_async(eta=self.object.start_time - timedelta(
            hours=HOURS_TO_CLOSE_APPLICATIONS))
        if self.object.gender != GenderChoices.MIXES.value:
            recalculate_rating_task.apply_async(
                (self.object.type,),
                eta=(self.object.end_time + timedelta(
                    hours=HOURS_TO_CLOSE_APPLICATIONS
                ))
            )
        return reverse_lazy('competition_type_choice')

    def get_context_data(self, **kwargs):
        kwargs['form'] = self.get_form()
        return kwargs


class ApplicationsView(TemplateView):
    template_name = "applications.html"

    def get_context_data(self, **kwargs):
        kwargs['applications'] = Application.objects.filter(
            competition__title=self.kwargs['competition_title']
        )
        kwargs['competition'] = Competition.objects.get(
            title=self.kwargs['competition_title']
        )
        return super().get_context_data(**kwargs)


class ApplicationAddView(FormView):
    template_name = "application_add.html"
    form_class = ApplicationAddForm

    def get_success_url(self):
        return reverse_lazy(
            'applications',
            kwargs={'competition_title': self.kwargs['competition_title']}
        )

    def form_valid(self, form):
        team = Team.objects.create(title=form.data['title'])
        competition = Competition.objects.get(
            title=self.kwargs['competition_title'])
        for player_id in form.data.getlist('player'):
            player = Player.objects.get(id=UUID(player_id))
            player.team.add(team)
        Application.objects.create(competition=competition,
                                   team=team)
        calculate_team_rating_task.delay(team.id, competition.type)
        return super().form_valid(form)


class ApplicationRemoveView(DeleteView):
    model = Application
    success_url = reverse_lazy('competition_type_choice')

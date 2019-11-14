from uuid import UUID

from competition.forms import (ApplicationAddForm, CompetitionChoiceForm,
                               CompetitionCreateForm)
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, FormView, TemplateView
from participant.models import Player, Team

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
                                                form.data['type']
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
            type=self.kwargs['competition_type']
        ).order_by('-created')
        return kwargs


class CompetitionCreateView(CreateView):
    template_name = "competition_create_form.html"
    form_class = CompetitionCreateForm
    success_url = reverse_lazy('competition_type_choice')

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
        return super().form_valid(form)


class ApplicationRemoveView(DeleteView):
    model = Application
    success_url = reverse_lazy('competition_type_choice')

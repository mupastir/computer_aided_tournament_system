from competition.forms import CompetitionChoiceForm, CompetitionCreateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, TemplateView

from .models import Application, Competition


class CompetitionChoiceView(FormView):
    template_name = "competition_choice.html"
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


class CompetitionCreateView(CreateView):

    template_name = "competition_create.html"
    form_class = CompetitionCreateForm
    template_name_suffix = None


class CompetitionFilteredView(CompetitionChoiceView):

    def get_context_data(self, **kwargs):
        kwargs['competitions'] = Competition.objects.filter(
            type=self.kwargs['competition_type']
        ).order_by('-created')
        return super().get_context_data(**kwargs)


class ApplicationsView(TemplateView):

    template_name = "applications.html"

    def get_context_data(self, **kwargs):
        kwargs['applications'] = Application.objects.filter(
            competition__title=self.kwargs['competition_title']
        )
        return super().get_context_data(**kwargs)

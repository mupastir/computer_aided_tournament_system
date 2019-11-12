from competition.forms import CompetitionChoiceForm
from django.views.generic import FormView


class CompetitionChoiceView(FormView):
    template_name = "competition_choice.html"
    form_class = CompetitionChoiceForm

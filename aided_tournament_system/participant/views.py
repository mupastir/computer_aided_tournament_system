from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView
from participant.forms import RatingChoiceForm
from participant.services.get_ratings import (get_rating_url,
                                              get_ratings_by_type_gender)
from participant.tasks import (create_player_task, create_referee_task,
                               player_join_team_task)


class RatingChoiceView(FormView):
    template_name = 'rating_list.html'
    form_class = RatingChoiceForm

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        self.success_url = get_rating_url(form.data['type'],
                                          form.data['gender'])
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['ratings_list'] = get_ratings_by_type_gender('Beach', 'w')
        return super().get_context_data(**kwargs)


class RatingView(RatingChoiceView):

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs['ratings_list'] = get_ratings_by_type_gender(
            self.kwargs['type'],
            self.kwargs['gender']
        )
        return kwargs


class RefereeCreateView(View):

    def post(self, request):
        create_referee_task.apply_async((request.user.id,))
        return redirect('/user/detail/')


class PlayerCreateView(View):

    def post(self, request):
        create_player_task.apply_async((request.user.id,))
        return redirect('/user/detail/')


class PlayerJoinToTeamView(View):

    def put(self, request, team_id):
        player_join_team_task.apply_async((team_id, request.user.id,))
        return redirect('/competitions/list/')

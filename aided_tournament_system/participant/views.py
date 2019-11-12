from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView, TemplateView
from participant.forms import RatingChoiceForm
from participant.models import Player, Referee, Team
from participant.services.get_ratings import (get_rating_url,
                                              get_ratings_by_type_gender)


class ChoiceRatingView(FormView):
    template_name = 'ratings.html'
    form_class = RatingChoiceForm

    def get_success_url(self):
        return super().get_success_url()

    def form_valid(self, form):
        self.success_url = get_rating_url(form.data['type'],
                                          form.data['gender'])
        return super().form_valid(form)


class RatingView(TemplateView):
    template_name = "rating_list.html"

    def get_context_data(self, **kwargs):
        kwargs['ratings_list'] = get_ratings_by_type_gender(kwargs['type'],
                                                            kwargs['gender'])


class RefereeCreateView(View):

    def post(self, request):
        Referee.objects.create(user_id=request.user.id)
        return redirect('/user/detail/')


class PlayerCreateView(View):

    def post(self, request):
        Player.objects.create(user_id=request.user.id)
        return redirect('/user/detail/')


class PlayerJoinToTeamView(View):

    def put(self, request, team_id):
        team = Team.objects.get(id=team_id)
        player = Player.objects.get(user_id=request.user.id)
        player.save()
        player.team.add(team)
        return redirect('/competitions/list/')

from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from game.models import Game
from game.tasks import move_teams_next_round_task
from participant.services.is_referee import is_referee


class GameListView(TemplateView):
    template_name = "game_list.html"

    def get_context_data(self, **kwargs):
        kwargs['games'] = Game.objects.filter(
            competition__title=self.kwargs['competition_title']
        ).order_by('game_number')
        kwargs['is_referee'] = is_referee(self.request.user.id)
        return super().get_context_data(**kwargs)


class GameScoreUpdate(UpdateView):
    template_name = "update_score.html"
    model = Game
    fields = ['home_team_score', 'away_team_score']

    def get_success_url(self):
        move_teams_next_round_task.apply_async((self.kwargs['pk'],))
        return reverse_lazy(
            'games_list',
            kwargs={
                'competition_title':
                    Game.objects.get(id=self.kwargs['pk']).competition.title
            }
        )

    def get_context_data(self, **kwargs):
        kwargs['game'] = Game.objects.get(id=self.kwargs['pk'])
        kwargs['is_referee'] = is_referee(self.request.user.id)
        return super().get_context_data(**kwargs)


class GameInfoUpdate(UpdateView):
    template_name = "update_game_info.html"
    model = Game
    fields = ['start_time',
              'end_time',
              'court_number']

    def get_success_url(self):
        move_teams_next_round_task.apply_async((self.kwargs['pk'],))
        return reverse_lazy(
            'games_list',
            kwargs={
                'competition_title':
                    Game.objects.get(id=self.kwargs['pk']).competition.title
            }
        )

    def get_context_data(self, **kwargs):
        kwargs['game'] = Game.objects.get(id=self.kwargs['pk'])
        return super().get_context_data(**kwargs)

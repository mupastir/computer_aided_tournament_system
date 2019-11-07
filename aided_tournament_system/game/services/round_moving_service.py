from uuid import UUID

from competition.models import Ranking
from game.models import Game
from participant.models import Team


class RoundMovingService:

    def __init__(self, game_id: UUID):
        self.game_id = game_id
        self.game = self._get_game()
        self.winner_team_id = self._get_winner_team()
        self.loser_team_id = self._get_loser_team()

    def move_teams(self):
        self.move_winner()
        self.move_loser()

    def move_winner(self):
        try:
            winner_reference_game_number = int(self.game.winner_ref)
            self._move_team_next_round(winner_reference_game_number,
                                       self.winner_team_id)
        except ValueError:
            if self.game.winner_ref == 'Final game':
                self._move_to_rankings(1, self.winner_team_id)
            else:
                self._move_to_rankings(3, self.winner_team_id)

    def move_loser(self):
        try:
            loser_reference_game_number = int(self.game.loser_ref)
            self._move_team_next_round(loser_reference_game_number,
                                       self.loser_team_id)
        except ValueError:
            self._move_loser_to_rankings()

    def _get_game(self):
        return Game.objects.get(id=self.game_id)

    def _get_winner_team(self) -> UUID:
        if self.game.home_team_score > self.game.away_team_score:
            return self.game.home_team_id
        return self.game.away_team_id

    def _get_loser_team(self) -> UUID:
        if self.game.home_team_score < self.game.away_team_score:
            return self.game.home_team_id
        return self.game.away_team_id

    def _move_team_next_round(self, game_number_ref: int, team_id: UUID):
        if Game.objects.get(competition=self.game.competition,
                            game_number=game_number_ref).home_team_id is None:
            Game.objects.filter(
                competition=self.game.competition,
                game_number=game_number_ref).update(
                home_team_id=team_id)
        else:
            Game.objects.filter(
                competition=self.game.competition,
                game_number=game_number_ref).update(
                away_team_id=team_id)

    def _move_loser_to_rankings(self):
        try:
            round_place = int(self.game.round_game)
            self._move_to_rankings(round_place, self.loser_team_id)
        except ValueError:
            if self.game.winner_ref == 'Final game':
                self._move_to_rankings(2, self.loser_team_id)
            else:
                self._move_to_rankings(4, self.loser_team_id)

    def _move_to_rankings(self, place: int, team_id: UUID):
        Ranking.objects.create(
            competition=self.game.competition,
            place=place,
            team=Team.objects.get(id=team_id))

from abc import ABC, abstractmethod
from uuid import UUID

from game.models import Game


class BaseTournament(ABC):

    def __init__(self, competition_id: UUID):
        self.competition_id = competition_id
        self.games_schedule = []

    def create_games_schedule(self):
        self._create_game_list()
        self._write_games_to_db()

    @abstractmethod
    def _create_game_list(self):
        pass

    def _add_game_to_schedule(self,
                              game_number: int,
                              round_game: str,
                              winner_ref: str,
                              loser_ref: str):
        self.games_schedule.append(
            Game(
                game_number=game_number,
                round_game=round_game,
                competition_id=self.competition_id,
                winner_ref=winner_ref,
                loser_ref=loser_ref
            )
        )

    def _write_games_to_db(self):
        Game.objects.bulk_create(self.games_schedule)

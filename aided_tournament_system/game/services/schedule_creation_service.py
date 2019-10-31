from abc import ABC, abstractmethod

from game.models import Game


class BaseScheduleCreator(ABC):
    SCHEDULE_SIZES_AVAILABLE = ['16', '32']

    def __init__(self, schedule_size: str):
        self.schedule_size = schedule_size

    @property
    def schedule_size(self):
        return self._schedule_size

    @schedule_size.setter
    def schedule_size(self, value):
        self._validate_schedule_size(value)
        self._schedule_size = value

    def _validate_schedule_size(self, schedule_size):
        if schedule_size not in self.SCHEDULE_SIZES_AVAILABLE:
            raise ValueError

    @staticmethod
    def create_game(game_number,
                    court_number,
                    home_team,
                    away_team,
                    start_time,
                    round_game):
        Game.objects.create(
            start_time=start_time,
            game_number=game_number,
            court_number=court_number,
            home_team=home_team,
            away_team=away_team,
            round_game=round_game
        )

    @abstractmethod
    def create_schedule(self):
        pass

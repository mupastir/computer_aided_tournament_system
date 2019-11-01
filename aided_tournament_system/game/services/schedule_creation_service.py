from abc import ABC, abstractmethod
from uuid import UUID

from game.models import Game


class BaseTournament(ABC):

    @staticmethod
    def create_game(game_number: int,
                    round_game: str,
                    competition_id: UUID,
                    winner_ref: str,
                    loser_ref: str):
        Game.objects.create(
            game_number=game_number,
            round_game=round_game,
            competition_id=competition_id,
            winner_ref=winner_ref,
            loser_ref=loser_ref
        )

    @abstractmethod
    def create_games_schedule(self, competition_id: UUID):
        pass


class Tournament32Teams(BaseTournament):

    def _create_first_winner_round_games(self, competition_id) -> None:
        self.create_game(game_number=1,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='9',
                         loser_ref='16')
        self.create_game(game_number=2,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='9',
                         loser_ref='16')
        self.create_game(game_number=3,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='10',
                         loser_ref='15')
        self.create_game(game_number=4,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='10',
                         loser_ref='15')
        self.create_game(game_number=5,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='11',
                         loser_ref='14')
        self.create_game(game_number=6,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='11',
                         loser_ref='14')
        self.create_game(game_number=7,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='12',
                         loser_ref='13')
        self.create_game(game_number=8,
                         round_game='I',
                         competition_id=competition_id,
                         winner_ref='2',
                         loser_ref='13')

    def _create_second_winner_round_games(self, competition_id):
        self.create_game(game_number=9,
                         round_game='II',
                         competition_id=competition_id,
                         winner_ref='21',
                         loser_ref='18')
        self.create_game(game_number=10,
                         round_game='II',
                         competition_id=competition_id,
                         winner_ref='21',
                         loser_ref='17')
        self.create_game(game_number=11,
                         round_game='II',
                         competition_id=competition_id,
                         winner_ref='22',
                         loser_ref='20')
        self.create_game(game_number=12,
                         round_game='II',
                         competition_id=competition_id,
                         winner_ref='22',
                         loser_ref='19')

    def _create_for_13_place_games(self, competition_id):
        self.create_game(game_number=13,
                         round_game='13',
                         competition_id=competition_id,
                         winner_ref='17',
                         loser_ref='')
        self.create_game(game_number=14,
                         round_game='13',
                         competition_id=competition_id,
                         winner_ref='18',
                         loser_ref='')
        self.create_game(game_number=15,
                         round_game='13',
                         competition_id=competition_id,
                         winner_ref='19',
                         loser_ref='')
        self.create_game(game_number=16,
                         round_game='13',
                         competition_id=competition_id,
                         winner_ref='20',
                         loser_ref='')

    def _create_for_9_place_games(self, competition_id):
        self.create_game(game_number=17,
                         round_game='9',
                         competition_id=competition_id,
                         winner_ref='23',
                         loser_ref='')
        self.create_game(game_number=18,
                         round_game='9',
                         competition_id=competition_id,
                         winner_ref='23',
                         loser_ref='')
        self.create_game(game_number=19,
                         round_game='9',
                         competition_id=competition_id,
                         winner_ref='24',
                         loser_ref='')
        self.create_game(game_number=10,
                         round_game='9',
                         competition_id=competition_id,
                         winner_ref='24',
                         loser_ref='')

    def _create_third_winner_round_games(self, competition_id):
        self.create_game(game_number=21,
                         round_game='III',
                         competition_id=competition_id,
                         winner_ref='27',
                         loser_ref='26')
        self.create_game(game_number=22,
                         round_game='III',
                         competition_id=competition_id,
                         winner_ref='28',
                         loser_ref='25')

    def _create_for_7_place_games(self, competition_id):
        self.create_game(game_number=23,
                         round_game='7',
                         competition_id=competition_id,
                         winner_ref='25',
                         loser_ref='')
        self.create_game(game_number=24,
                         round_game='7',
                         competition_id=competition_id,
                         winner_ref='26',
                         loser_ref='')

    def _create_for_5_place_games(self, competition_id):
        self.create_game(game_number=25,
                         round_game='5',
                         competition_id=competition_id,
                         winner_ref='27',
                         loser_ref='')
        self.create_game(game_number=26,
                         round_game='5',
                         competition_id=competition_id,
                         winner_ref='28',
                         loser_ref='')

    def _create_semi_final_games(self, competition_id):
        self.create_game(game_number=27,
                         round_game='SF',
                         competition_id=competition_id,
                         winner_ref='30',
                         loser_ref='29')
        self.create_game(game_number=28,
                         round_game='SF',
                         competition_id=competition_id,
                         winner_ref='30',
                         loser_ref='29')

    def _create_final_games(self, competition_id):
        self.create_game(game_number=29,
                         round_game='3/4',
                         competition_id=competition_id,
                         winner_ref='',
                         loser_ref='')
        self.create_game(game_number=30,
                         round_game='F',
                         competition_id=competition_id,
                         winner_ref='',
                         loser_ref='')

    def create_games_schedule(self, competition_id: UUID) -> None:
        self._create_first_winner_round_games(competition_id)
        self._create_second_winner_round_games(competition_id)
        self._create_for_13_place_games(competition_id)
        self._create_for_9_place_games(competition_id)
        self._create_third_winner_round_games(competition_id)
        self._create_for_7_place_games(competition_id)
        self._create_for_5_place_games(competition_id)
        self._create_semi_final_games(competition_id)
        self._create_final_games(competition_id)


class Tournament16Teams(BaseTournament):

    def create_games_schedule(self, competition_id: UUID):
        pass


SCHEDULE_SIZES_AVAILABLE = {'16': Tournament32Teams,
                            '32': Tournament16Teams}


class TournamentGames:

    def __init__(self, schedule_size: str, competition_id: UUID):
        self.schedule_size = schedule_size
        self.competition_id = competition_id
        self.schedule_creator = SCHEDULE_SIZES_AVAILABLE.get(
            self.schedule_size
        )

    @property
    def schedule_size(self):
        return self._schedule_size

    @schedule_size.setter
    def schedule_size(self, value):
        self._validate_schedule_size(value)
        self._schedule_size = value

    @staticmethod
    def _validate_schedule_size(schedule_size):
        if schedule_size not in SCHEDULE_SIZES_AVAILABLE.keys():
            raise ValueError

    def create_schedule(self):
        self.schedule_creator().create_games_schedule(self.competition_id)

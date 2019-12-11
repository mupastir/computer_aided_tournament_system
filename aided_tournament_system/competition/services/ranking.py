from uuid import UUID

from competition.models import Competition, Ranking
from competition.services.constants import (Ranking8Teams, Ranking16Teams,
                                            Ranking32Teams)


class Ranking8TeamsCreator:
    rankings = Ranking8Teams

    def __init__(self, competition: Competition):
        self.competition = competition
        self.ranking_list = []

    def _create_first_four_ranking(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=place_i+1,
            ranking=(self.rankings.FIRST_PLACE - place_i)
        ) for place_i in range(4)])

    def _create_fifth_place_ranking(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=5,
            ranking=self.rankings.FIFTH_PLACE
        ) for _ in range(2)])

    def _create_seventh_place_ranking(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=7,
            ranking=self.rankings.SEVENTH_PLACE
        ) for _ in range(2)])

    def create(self):
        self._create_first_four_ranking()
        self._create_fifth_place_ranking()
        self._create_seventh_place_ranking()

    def save_to_db(self):
        Ranking.objects.bulk_create(self.ranking_list)


class Ranking16TeamsCreator(Ranking8TeamsCreator):
    rankings = Ranking16Teams

    def _create_ninth_place_ranking(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=9,
            ranking=self.rankings.NINTH_PLACE
        ) for _ in range(4)])

    def _create_thirteenth_place(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=13,
            ranking=self.rankings.THIRTEENTH_PLACE
        ) for _ in range(4)])

    def create(self):
        super().create()
        self._create_ninth_place_ranking()
        self._create_thirteenth_place()


class Ranking32TeamsCreator(Ranking16TeamsCreator):
    rankings = Ranking32Teams

    def _create_seventeenth_place(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=17,
            ranking=self.rankings.SEVENTEENTH_PLACE
        ) for _ in range(8)])

    def _create_twenty_fifth_place(self):
        self.ranking_list.extend([Ranking(
            competition=self.competition,
            place=25,
            ranking=self.rankings.TWENTY_FIFTH_PLACE
        ) for _ in range(8)])

    def create(self):
        super().create()
        self._create_seventeenth_place()
        self._create_twenty_fifth_place()


RANKING_CHOICES = {8: Ranking8TeamsCreator,
                   16: Ranking16TeamsCreator,
                   32: Ranking32TeamsCreator}


def ranking_creating_service(competition_id: UUID) -> None:
    competition = Competition.objects.get(id=competition_id)
    ranking_creator = RANKING_CHOICES[
        int(competition.schedule_system)
    ](competition)
    ranking_creator.create()
    ranking_creator.save_to_db()

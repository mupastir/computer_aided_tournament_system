from game.choices import RoundChoices
from game.services.schedule_creation_services.base_schedule import BaseTournament

SCHEDULE_SIZES_AVAILABLE = {}


def register_tournament(key):
    def inner(tournament):
        SCHEDULE_SIZES_AVAILABLE[key] = tournament
        return tournament

    return inner


@register_tournament("32")
class Tournament32Teams(BaseTournament):
    def _create_game_list(self):
        self._create_first_winner_round_games()
        self._create_second_winner_round_games()
        self._create_for_25_place_games()
        self._create_for_17_place_games()
        self._create_third_winner_round_games()
        self._create_for_13_place_games()
        self._create_for_9_place_games()
        self._create_fourth_winner_round_games()
        self._create_for_7_place_games()
        self._create_for_5_place_games()
        self._create_semi_final_games()
        self._create_final_games()

    def _create_first_winner_round_games(
        self,
    ):
        self._add_game_to_schedule(
            game_number=1,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="17",
            loser_ref="25",
        )
        self._add_game_to_schedule(
            game_number=2,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="17",
            loser_ref="25",
        )
        self._add_game_to_schedule(
            game_number=3,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="18",
            loser_ref="26",
        )
        self._add_game_to_schedule(
            game_number=4,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="18",
            loser_ref="26",
        )
        self._add_game_to_schedule(
            game_number=5,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="19",
            loser_ref="27",
        )
        self._add_game_to_schedule(
            game_number=6,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="19",
            loser_ref="27",
        )
        self._add_game_to_schedule(
            game_number=7,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="20",
            loser_ref="28",
        )
        self._add_game_to_schedule(
            game_number=8,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="20",
            loser_ref="28",
        )
        self._add_game_to_schedule(
            game_number=9,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="21",
            loser_ref="29",
        )
        self._add_game_to_schedule(
            game_number=10,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="21",
            loser_ref="29",
        )
        self._add_game_to_schedule(
            game_number=11,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="22",
            loser_ref="30",
        )
        self._add_game_to_schedule(
            game_number=12,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="22",
            loser_ref="30",
        )
        self._add_game_to_schedule(
            game_number=13,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="23",
            loser_ref="31",
        )
        self._add_game_to_schedule(
            game_number=14,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="23",
            loser_ref="31",
        )
        self._add_game_to_schedule(
            game_number=15,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="24",
            loser_ref="32",
        )
        self._add_game_to_schedule(
            game_number=16,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="24",
            loser_ref="32",
        )

    def _create_second_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=17,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="41",
            loser_ref="40",
        )
        self._add_game_to_schedule(
            game_number=18,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="41",
            loser_ref="39",
        )
        self._add_game_to_schedule(
            game_number=19,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="42",
            loser_ref="38",
        )
        self._add_game_to_schedule(
            game_number=20,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="42",
            loser_ref="37",
        )
        self._add_game_to_schedule(
            game_number=21,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="43",
            loser_ref="36",
        )
        self._add_game_to_schedule(
            game_number=22,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="43",
            loser_ref="35",
        )
        self._add_game_to_schedule(
            game_number=23,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="44",
            loser_ref="34",
        )
        self._add_game_to_schedule(
            game_number=24,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="44",
            loser_ref="33",
        )

    def _create_for_25_place_games(self):
        self._add_game_to_schedule(
            game_number=25,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="33",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=26,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="34",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=27,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="35",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=28,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="36",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=29,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="37",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=30,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="38",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=31,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="39",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=32,
            round_game=RoundChoices.FOR_25_PLACE.value,
            winner_ref="40",
            loser_ref="",
        )

    def _create_for_17_place_games(self):
        self._add_game_to_schedule(
            game_number=33,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="45",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=34,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="45",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=35,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="46",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=36,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="46",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=37,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="47",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=38,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="47",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=39,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="48",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=40,
            round_game=RoundChoices.FOR_17_PLACE.value,
            winner_ref="48",
            loser_ref="",
        )

    def _create_third_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=41,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="53",
            loser_ref="50",
        )
        self._add_game_to_schedule(
            game_number=42,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="53",
            loser_ref="49",
        )
        self._add_game_to_schedule(
            game_number=43,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="54",
            loser_ref="52",
        )
        self._add_game_to_schedule(
            game_number=44,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="54",
            loser_ref="51",
        )

    def _create_for_13_place_games(self):
        self._add_game_to_schedule(
            game_number=45,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="49",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=46,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="50",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=47,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="51",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=48,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="52",
            loser_ref="",
        )

    def _create_for_9_place_games(self):
        self._add_game_to_schedule(
            game_number=49,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="55",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=50,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="55",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=51,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="56",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=52,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="56",
            loser_ref="",
        )

    def _create_fourth_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=53,
            round_game=RoundChoices.THIRD_ROUND.value,
            winner_ref="59",
            loser_ref="58",
        )
        self._add_game_to_schedule(
            game_number=54,
            round_game=RoundChoices.THIRD_ROUND.value,
            winner_ref="60",
            loser_ref="57",
        )

    def _create_for_7_place_games(self):
        self._add_game_to_schedule(
            game_number=55,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="57",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=56,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="58",
            loser_ref="",
        )

    def _create_for_5_place_games(self):
        self._add_game_to_schedule(
            game_number=57,
            round_game=RoundChoices.FOR_5_PLACE.value,
            winner_ref="59",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=58,
            round_game=RoundChoices.FOR_5_PLACE.value,
            winner_ref="60",
            loser_ref="",
        )

    def _create_semi_final_games(self):
        self._add_game_to_schedule(
            game_number=59,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="62",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=60,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="61",
            loser_ref="",
        )

    def _create_final_games(self):
        self._add_game_to_schedule(
            game_number=61,
            round_game=RoundChoices.THREE_FOUR_PLACE.value,
            winner_ref="",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=62,
            round_game=RoundChoices.FINAL_ROUND.value,
            winner_ref="",
            loser_ref="",
        )


@register_tournament("16")
class Tournament16Teams(BaseTournament):
    def _create_game_list(self) -> None:
        self._create_first_winner_round_games()
        self._create_second_winner_round_games()
        self._create_for_13_place_games()
        self._create_for_9_place_games()
        self._create_third_winner_round_games()
        self._create_for_7_place_games()
        self._create_for_5_place_games()
        self._create_semi_final_games()
        self._create_final_games()

    def _create_first_winner_round_games(self) -> None:
        self._add_game_to_schedule(
            game_number=1,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="9",
            loser_ref="16",
        )
        self._add_game_to_schedule(
            game_number=2,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="9",
            loser_ref="16",
        )
        self._add_game_to_schedule(
            game_number=3,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="10",
            loser_ref="15",
        )
        self._add_game_to_schedule(
            game_number=4,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="10",
            loser_ref="15",
        )
        self._add_game_to_schedule(
            game_number=5,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="11",
            loser_ref="14",
        )
        self._add_game_to_schedule(
            game_number=6,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="11",
            loser_ref="14",
        )
        self._add_game_to_schedule(
            game_number=7,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="12",
            loser_ref="13",
        )
        self._add_game_to_schedule(
            game_number=8,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="2",
            loser_ref="13",
        )

    def _create_second_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=9,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="21",
            loser_ref="18",
        )
        self._add_game_to_schedule(
            game_number=10,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="21",
            loser_ref="17",
        )
        self._add_game_to_schedule(
            game_number=11,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="22",
            loser_ref="20",
        )
        self._add_game_to_schedule(
            game_number=12,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="22",
            loser_ref="19",
        )

    def _create_for_13_place_games(self):
        self._add_game_to_schedule(
            game_number=13,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="17",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=14,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="18",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=15,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="19",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=16,
            round_game=RoundChoices.FOR_13_PLACE.value,
            winner_ref="20",
            loser_ref="",
        )

    def _create_for_9_place_games(self):
        self._add_game_to_schedule(
            game_number=17,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="23",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=18,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="23",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=19,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="24",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=10,
            round_game=RoundChoices.FOR_9_PLACE.value,
            winner_ref="24",
            loser_ref="",
        )

    def _create_third_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=21,
            round_game=RoundChoices.THIRD_ROUND.value,
            winner_ref="27",
            loser_ref="26",
        )
        self._add_game_to_schedule(
            game_number=22,
            round_game=RoundChoices.THIRD_ROUND.value,
            winner_ref="28",
            loser_ref="25",
        )

    def _create_for_7_place_games(self):
        self._add_game_to_schedule(
            game_number=23,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="25",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=24,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="26",
            loser_ref="",
        )

    def _create_for_5_place_games(self):
        self._add_game_to_schedule(
            game_number=25,
            round_game=RoundChoices.FOR_5_PLACE.value,
            winner_ref="27",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=26,
            round_game=RoundChoices.FOR_5_PLACE.value,
            winner_ref="28",
            loser_ref="",
        )

    def _create_semi_final_games(self):
        self._add_game_to_schedule(
            game_number=27,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="30",
            loser_ref="29",
        )
        self._add_game_to_schedule(
            game_number=28,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="30",
            loser_ref="29",
        )

    def _create_final_games(self):
        self._add_game_to_schedule(
            game_number=29,
            round_game=RoundChoices.THREE_FOUR_PLACE.value,
            winner_ref="",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=30,
            round_game=RoundChoices.FINAL_ROUND.value,
            winner_ref="",
            loser_ref="",
        )


@register_tournament("8")
class Tournament8Teams(BaseTournament):
    def _create_game_list(self):
        self._create_first_winner_round_games()
        self._create_second_winner_round_games()
        self._create_for_7_place_games()
        self._create_for_5_place_games()
        self._create_semi_final_games()
        self._create_final_games()

    def _create_first_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=1,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="5",
            loser_ref="7",
        )
        self._add_game_to_schedule(
            game_number=2,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="5",
            loser_ref="7",
        )
        self._add_game_to_schedule(
            game_number=3,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="6",
            loser_ref="8",
        )
        self._add_game_to_schedule(
            game_number=4,
            round_game=RoundChoices.FIRST_ROUND.value,
            winner_ref="6",
            loser_ref="8",
        )

    def _create_second_winner_round_games(self):
        self._add_game_to_schedule(
            game_number=5,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="11",
            loser_ref="9",
        )
        self._add_game_to_schedule(
            game_number=6,
            round_game=RoundChoices.SECOND_ROUND.value,
            winner_ref="12",
            loser_ref="10",
        )

    def _create_for_7_place_games(self):
        self._add_game_to_schedule(
            game_number=7,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="9",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=8,
            round_game=RoundChoices.FOR_7_PLACE.value,
            winner_ref="10",
            loser_ref="",
        )

    def _create_for_5_place_games(self):
        self._add_game_to_schedule(
            game_number=9,
            round_game=RoundChoices.FOR_5_PLACE.value,
            winner_ref="11",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=10, round_game="12", winner_ref="28", loser_ref=""
        )

    def _create_semi_final_games(self):
        self._add_game_to_schedule(
            game_number=11,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="14",
            loser_ref="13",
        )
        self._add_game_to_schedule(
            game_number=12,
            round_game=RoundChoices.SEMIFINAL.value,
            winner_ref="14",
            loser_ref="13",
        )

    def _create_final_games(self):
        self._add_game_to_schedule(
            game_number=13,
            round_game=RoundChoices.THREE_FOUR_PLACE.value,
            winner_ref="",
            loser_ref="",
        )
        self._add_game_to_schedule(
            game_number=14,
            round_game=RoundChoices.FINAL_ROUND.value,
            winner_ref="",
            loser_ref="",
        )

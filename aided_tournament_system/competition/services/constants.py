from dataclasses import dataclass


@dataclass
class Rankings:
    FIRST_PLACE = 0
    FIFTH_PLACE = 0
    LAST_PLACE = 0


class Ranking8Teams(Rankings):
    FIRST_PLACE = 6
    FIFTH_PLACE = 2
    SEVENTH_PLACE = 0


class Ranking16Teams(Rankings):
    FIRST_PLACE = 8
    FIFTH_PLACE = 4
    SEVENTH_PLACE = 3
    NINTH_PLACE = 2
    THIRTEENTH_PLACE = 0


class Ranking32Teams(Rankings):
    FIRST_PLACE = 10
    FIFTH_PLACE = 6
    SEVENTH_PLACE = 5
    NINTH_PLACE = 4
    THIRTEENTH_PLACE = 3
    SEVENTEENTH_PLACE = 2
    TWENTY_FIFTH_PLACE = 0

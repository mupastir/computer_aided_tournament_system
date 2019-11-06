from django_utils.choices import BaseChoices, StrChoice


class RoundChoices(BaseChoices):
    FIRST_ROUND = StrChoice('I', 'First round')
    SECOND_ROUND = StrChoice('II', 'Second round')
    THIRD_ROUND = StrChoice('III', 'Third round')
    FOURTH_ROUND = StrChoice('IV', 'Fourth round')
    FOR_25_PLACE = StrChoice('25', 'Loser 25 place game')
    FOR_17_PLACE = StrChoice('17', 'Loser 17 place game')
    FOR_13_PLACE = StrChoice('13', 'Loser 13 place game')
    FOR_9_PLACE = StrChoice('9', 'Loser 9 place game')
    FOR_7_PLACE = StrChoice('7', 'Loser 7 place game')
    FOR_5_PLACE = StrChoice('5', 'Loser 5 place game')
    SEMIFINAL = StrChoice('SF', 'Semi-final game')
    THREE_FOUR_PLACE = StrChoice('3/4', 'Game 3/4 places')
    FINAL_ROUND = StrChoice('F', 'Final game')

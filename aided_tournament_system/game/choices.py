from django_utils.choices import BaseChoices


class RoundChoices(BaseChoices):
    FIRST_ROUND = ('I', 'First round')
    SECOND_ROUND = ('II', 'Second round')
    THIRD_ROUND = ('III', 'Third round')
    LOSER_FIRST_ROUND = ('13', 'Loser 13 place game')
    LOSER_SECOND_ROUND = ('9', 'Loser 9 place game')
    LOSER_THIRD_ROUND = ('7', 'Loser 7 place game')
    LOSER_FOURTH_ROUND = ('5', 'Loser 5 place game')
    SEMIFINAL = ('SF', 'Semi-final game')
    THREE_FOUR_PLACE = ('3/4', 'Game 3/4 places')
    FINAL_ROUND = ('F', 'Final game')

from game.models import Game
from rest_framework import serializers


class UpdateGameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['home_team_score',
                  'away_team_score']

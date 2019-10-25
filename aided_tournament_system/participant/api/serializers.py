from rest_framework import serializers
from ..models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
    fields = ['first_name', 'last_name', 'uuid', 'sex', 'country',
              'rating', 'email']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
    fields = ['uuid', 'title', 'player', 'rating', 'games']

from rest_framework import serializers

from ..models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'id', 'sex', 'country',
                  'rating', 'email']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'title', 'player', 'rating', 'games']

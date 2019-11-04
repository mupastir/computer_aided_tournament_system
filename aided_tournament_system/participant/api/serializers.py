from rest_framework import serializers

from ..models import Player, Referee, Team


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'sex', 'country',
                  'rating']


class RefereeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['first_name', 'last_name']


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title', 'rating']

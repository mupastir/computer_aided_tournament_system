from rest_framework import serializers

from ..models import Player, Referee, Team


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['rating']


class RefereeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = []


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title', 'rating']


class PlayerInTeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['last_name', 'first_name', 'team.title']


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = []


class RefereeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = []


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['title']

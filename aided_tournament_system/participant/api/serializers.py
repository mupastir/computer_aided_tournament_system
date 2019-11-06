from participant.models import Player, Referee, Team
from rest_framework import serializers


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'rating']
        read_only_fields = ['id']


class RefereeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['id']
        read_only_fields = ['id']


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'title', 'rating']
        read_only_fields = ['id']


class PlayerInTeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['last_name', 'first_name', 'team.title']


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id']
        read_only_fields = ['id']


class RefereeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ['id']
        read_only_fields = ['id']


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'title']
        read_only_fields = ['id']

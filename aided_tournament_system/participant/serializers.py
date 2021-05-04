from participant.models import Player, Rating, Referee, Team
from rest_framework import serializers
from user_auth.serializers import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ["id", "type", "points"]
        read_only_fileds = ["id"]


class PlayerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    rating = RatingSerializer(many=True)

    class Meta:
        model = Player
        fields = ["id", "rating", "user"]
        read_only_fields = ["id"]


class RefereeListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Referee
        fields = ["id", "user"]
        read_only_fields = ["id", "user"]


class TeamListSerializer(serializers.ModelSerializer):
    players = PlayerListSerializer(many=True)

    class Meta:
        model = Team
        fields = ["id", "title", "rating", "players"]
        read_only_fields = ["id"]


class PlayerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["id"]
        read_only_fields = ["id"]


class RefereeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referee
        fields = ["id"]
        read_only_fields = ["id"]


class TeamCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "title"]
        read_only_fields = ["id"]

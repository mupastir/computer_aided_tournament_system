from competition.models import Application, Competition, Ranking
from rest_framework import serializers


class CompetitionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ["id", "title", "start_time", "end_time"]
        read_only_fields = ["id"]


class CompetitionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = [
            "id",
            "title",
            "start_time",
            "end_time",
            "schedule_system",
            "courts_number",
            "gender",
        ]
        read_only_fields = ["id"]


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ["id", "team.title", "competition.title", "is_open"]
        read_only_fields = ["id"]


class RankingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ["id", "competition.title", "team.title", "place", "ranking"]
        read_only_fields = ["id"]

from competition.models import Application, Competition, Ranking
from rest_framework import serializers


class CompetitionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['title',
                  'start_time',
                  'end_time']


class CompetitionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = ['title',
                  'start_time',
                  'end_time',
                  'schedule_system',
                  'courts_number',
                  'gender']


class ApplicationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['team.title',
                  'competition.title',
                  'is_open']


class RankingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = ['competition.title',
                  'team.title',
                  'place',
                  'ranking']

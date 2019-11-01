from competition.models import Competition
from game.services.schedule_creation_service import TournamentGames
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import CompetitionCreateSerializer, CompetitionListSerializer


class CompetitionListAPIView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer


class CompetitionCreateAPIView(CreateAPIView):
    serializer_class = CompetitionCreateSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        title = request.data.get('title')
        query_id = Competition\
            .objects\
            .filter(title=title)\
            .values('id', 'schedule_system')
        competition_id = query_id[0].get('id')
        schedule_system = query_id[0].get('schedule_system')
        tournament_games = TournamentGames(schedule_system, competition_id)
        tournament_games.create_schedule()

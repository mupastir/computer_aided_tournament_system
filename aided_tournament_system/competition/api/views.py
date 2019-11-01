from competition.models import Competition
from game.services.schedule_creation_service import TournamentGames
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .serializers import CompetitionCreateSerializer, CompetitionListSerializer


class CompetitionListAPIView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer
    permission_classes = (AllowAny,)


class CompetitionCreateAPIView(CreateAPIView):
    serializer_class = CompetitionCreateSerializer
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        title = request.data.get('title')
        query_id = Competition\
            .objects\
            .filter(title=title)\
            .values('id', 'schedule_system')
        competition_id = query_id[0].get('id')
        schedule_system = query_id[0].get('schedule_system')
        tournament_games = TournamentGames(schedule_system, competition_id)
        tournament_games.create_schedule()
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

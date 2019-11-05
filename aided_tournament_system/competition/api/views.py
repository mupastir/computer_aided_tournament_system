from competition.models import Competition
from game.services.schedule_creation_services.schedule_creator import \
    ScheduleCreator
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import CompetitionCreateSerializer, CompetitionListSerializer


class CompetitionListAPIView(ListAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionListSerializer
    permission_classes = (AllowAny,)


class CompetitionCreateAPIView(CreateAPIView):
    serializer_class = CompetitionCreateSerializer
    permission_classes = (IsAdminUser,)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        competition = serializer.instance
        tournament_games = ScheduleCreator(competition.schedule_system,
                                           competition.id)
        tournament_games.create_schedule()

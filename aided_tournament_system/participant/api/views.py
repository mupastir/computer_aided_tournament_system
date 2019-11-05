from participant.models import Player, Referee, Team
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import (PlayerInTeamListSerializer, PlayerListSerializer,
                          RefereeListSerializer, TeamListSerializer)


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = PlayerListSerializer


class RefereeListAPIView(ListAPIView):
    queryset = Referee.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RefereeListSerializer


class TeamListAPIView(ListAPIView):
    queryset = Team.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = TeamListSerializer


class PlayersInTeamsListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PlayerInTeamListSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Player.objects.filter(team__title=title)

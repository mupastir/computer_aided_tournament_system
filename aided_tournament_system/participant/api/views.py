from participant.models import Player, Referee, Team
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .serializers import (PlayerListSerializer, RefereeListSerializer,
                          TeamListSerializer)


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

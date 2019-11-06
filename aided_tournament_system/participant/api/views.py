from participant.models import Player, Referee, Team
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (PlayerInTeamListSerializer, PlayerListSerializer,
                          RefereeListSerializer, TeamCreateSerializer,
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


class PlayersInTeamsListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PlayerInTeamListSerializer

    def get_queryset(self):
        title = self.kwargs['title']
        return Player.objects.filter(team__title=title)


class PlayerCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Player.objects.create(user_id=request.user.id)
        return Response(data={'detail': 'Player has successfully created.'},
                        status=status.HTTP_201_CREATED)


class RefereeCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Referee.objects.create(user_id=request.user.id)
        return Response(data={'detail': 'Referee has successfully created.'},
                        status=status.HTTP_201_CREATED)


class TeamCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamCreateSerializer


class PlayerJoinToTeamAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, team_id):
        team = Team.objects.get(id=team_id)
        player = Player.objects.get(user_id=request.user.id)
        player.save()
        player.team.add(team)
        return Response(data={
            'detail': f'You successfully added to {team.title}.'
        })

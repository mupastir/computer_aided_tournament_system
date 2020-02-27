from participant.models import Player, Referee, Team
from participant.tasks import add_rating_to_player_task
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (PlayerListSerializer, RefereeListSerializer,
                          TeamCreateSerializer, TeamListSerializer)


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


class PlayerCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        player = Player.objects.create(user=request.user)
        add_rating_to_player_task.apply_async((player,))
        return Response(data={'detail': 'Player has successfully created.'},
                        status=status.HTTP_201_CREATED)


class RefereeCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Referee.objects.create(user=request.user)
        return Response(data={'detail': 'Referee has successfully created.'},
                        status=status.HTTP_201_CREATED)


class TeamCreateAPIView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TeamCreateSerializer


class PlayerJoinToTeamAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, team_id):
        team = Team.objects.get(id=team_id)
        player = Player.objects.get(user=request.user)
        player.save()
        player.team.add(team)
        return Response(data={
            'detail': f'You successfully added to team with id {team_id}.'
        })

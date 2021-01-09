from rest_framework import status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from participant.models import Player, Referee, Team
from participant.services.add_rating_to_player import add_rating_to_player
from participant.serializers import (PlayerCreateSerializer, PlayerListSerializer,
                          RefereeCreateSerializer, RefereeListSerializer,
                          TeamCreateSerializer, TeamListSerializer)


class PlayerApiViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser, IsAuthenticatedOrReadOnly)

    def list(self, request):
        queryset = Player.objects.all()
        serializer = PlayerListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        player = Player.objects.create(user=request.user)
        serializer = PlayerCreateSerializer(player)
        add_rating_to_player(player)
        headers = {'Location': f'/api/participant/players/{player.id}/'}
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class RefereeApiViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser, IsAuthenticatedOrReadOnly)

    def list(self, request):
        queryset = Referee.objects.all()
        serializer = RefereeListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        referee = Referee.objects.create(user=request.user)
        serializer = RefereeCreateSerializer(referee)
        headers = {'Location': f'/api/participant/referees/{referee.id}/'}
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class TeamApiViewSet(viewsets.ViewSet):
    permission_classes = (IsAdminUser, IsAuthenticatedOrReadOnly)

    def list(self, request):
        queryset = Team.objects.all()
        serializer = TeamListSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        team = Team.objects.create(title=data['title'])
        serializer = TeamCreateSerializer(team)
        headers = {'Location': f'/api/participant/referees/{team.id}/'}
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)

    def partial_update(self, request, team_id=None, player_id=None):
        team = Team.objects.get(id=team_id)
        player = Player.objects.get(id=player_id)
        team.players.add(player)
        team.save()
        serializer = TeamListSerializer(team)
        return Response(serializer.data, status=status.HTTP_200_OK)


player_list = PlayerApiViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


player_detail = PlayerApiViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


referee_list = RefereeApiViewSet.as_view({
    'get': 'list',
    'post': 'create'
})


referee_detail = RefereeApiViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


team_list = TeamApiViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

team_squad = TeamApiViewSet.as_view({
    'put': 'partial_update'
})

from django.shortcuts import get_object_or_404
from django_utils.permissions import IsRefereeScorerOrAdmin
from game.api.serializers import GameSerializer
from game.models import Game
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class GameAPIView(viewsets.ViewSet):
    permission_classes = (IsRefereeScorerOrAdmin, IsAuthenticated,)

    def get(self, request, pk=None):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        game.home_team_score = request.data['home_team_score']
        game.away_team_score = request.data['away_team_score']
        game.save()
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        queryset = Game.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

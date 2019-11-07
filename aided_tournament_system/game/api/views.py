from django_utils.permisions import IsRefereeScorerOrAdmin
from game.api.serializers import UpdateGameScoreSerializer
from game.models import Game
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated


class UpdateScoreForGameAPIView(UpdateAPIView):
    permission_classes = (IsRefereeScorerOrAdmin, IsAuthenticated,)
    serializer_class = UpdateGameScoreSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Game.objects.filter(pk=pk)

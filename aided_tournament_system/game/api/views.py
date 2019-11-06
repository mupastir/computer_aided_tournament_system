from django_utils.permisions import IsRefereeScorerOrAdmin
from game.api.serializers import UpdateGameScoreSerializer
from game.models import Game
from rest_framework.generics import UpdateAPIView


class UpdateScoreForGameAPIView(UpdateAPIView):
    permission_classes = (IsRefereeScorerOrAdmin,)
    serializer_class = UpdateGameScoreSerializer

    def get_queryset(self):
        game_id = self.kwargs['pk']
        return Game.objects.filter(pk=game_id)

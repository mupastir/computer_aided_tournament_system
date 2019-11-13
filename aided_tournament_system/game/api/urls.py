from django.conf.urls import url
from game.api import views

urlpatterns = [
    url(
        regex=r'^(?P<pk>.+)/update_score/$',
        view=views.UpdateScoreForGameAPIView.as_view(),
        name='update_game_score_api'
    )
]

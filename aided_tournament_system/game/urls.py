from django.conf.urls import url
from game import views

urlpatterns = [
    url(
        regex=r'^(?P<pk>.+)/update_score/$',
        view=views.GameScoreUpdate.as_view(),
        name='update_game_score'
    ),
    url(
        regex=r'^(?P<pk>.+)/update_game/$',
        view=views.GameInfoUpdate.as_view(),
        name='update_game_info'
    ),
    url(
        regex=r'^(?P<competition_title>.+)/$',
        view=views.GameListView.as_view(),
        name='games_list'
    )
]

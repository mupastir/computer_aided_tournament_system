from django.conf.urls import url
from participant.api import views

urlpatterns = [
    url(
        regex=r'^player/detail/$',
        view=views.PlayerListAPIView.as_view(),
        name='player_list'
    ),
    url(
        regex=r'^referee/detail/$',
        view=views.RefereeListAPIView.as_view(),
        name='referee_list'
    ),
    url(
        regex=r'^team/detail/$',
        view=views.TeamListAPIView.as_view(),
        name='team_list'
    ),
    url(
        regex=r'^team/(?P<title>.+)/players/$',
        view=views.PlayersInTeamsListAPIView.as_view(),
        name='players_in_team'
    ),
    url(
        regex=r'^player/add/$',
        view=views.PlayerCreateAPIView.as_view(),
        name='add_player_role'
    ),
    url(
        regex=r'^referee/add/$',
        view=views.RefereeCreateAPIView.as_view(),
        name='add_referee_role'
    ),
    url(
        regex=r'^team/create/$',
        view=views.TeamCreateAPIView.as_view(),
        name='create_team'
    ),
    url(
        regex=r'^join_to_team/(?P<team_id>.+)/$',
        view=views.PlayerJoinToTeamAPIView.as_view(),
        name='join_player_to_team'
    )
]

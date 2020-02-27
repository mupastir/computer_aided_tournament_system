from django.conf.urls import url
from participant.api import views

urlpatterns = [
    url(
        regex=r'^players/$',
        view=views.player_list,
        name='player_list'
    ),
    url(
        regex=r'^players/(?P<id>.+)/$',
        view=views.player_detail,
        name='player_detail'
    ),
    url(
        regex=r'^referees/$',
        view=views.referee_list,
        name='referee_list'
    ),
    url(
        regex=r'^referees/(?P<id>.+)/$',
        view=views.referee_detail,
        name='referee_detail'
    ),
    url(
        regex=r'^teams/$',
        view=views.team_list,
        name='team_list'
    ),
    url(
        regex=r'^teams/(?P<team_id>.+)/player/(?P<player_id>.+)/$',
        view=views.team_squad,
        name='join_player_to_team'
    )
]

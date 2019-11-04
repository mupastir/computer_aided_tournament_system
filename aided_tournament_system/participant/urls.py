from django.conf.urls import url

from .api import views

urlpatterns = [
    url(
        regex=r'^player/detail/$',
        view=views.PlayerListAPIView.as_view(),
        name='player_list_rest_api'
    ),
    url(
        regex=r'^referee/detail/$',
        view=views.RefereeListAPIView.as_view(),
        name='referee_list_rest_api_1'
    ),
    # /player/api/:slug/
    url(
        regex=r'^team/detail/$',
        view=views.TeamListAPIView.as_view(),
        name='team_list_rest_api_2'
    )
]

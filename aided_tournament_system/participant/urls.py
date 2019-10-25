from django.conf.urls import url

from .api import views

urlpatterns = [
    # /player/api/
    url(
        regex=r'^player/api/$',
        view=views.PlayerLookAPIView.as_view(),
        name='player_rest_api'
    ),
    # /player/api/:slug/
    url(
        regex=r'^player/api/(?P<uuid>[-\w]+)/$',
        view=views.PlayerCreateAPIView.as_view(),
        name='player_rest_api'
    ),
    # /team/api/
    url(
        regex=r'^team/api/$',
        view=views.TeamListCreateAPIView.as_view(),
        name='team_rest_api'
    ),
    # /team/api/:slug/
    url(
        regex=r'^team/api/(?P<uuid>[-\w]+)/$',
        view=views.TeamRetrieveUpdateDestroyAPIView.as_view(),
        name='team_rest_api'
    )
]

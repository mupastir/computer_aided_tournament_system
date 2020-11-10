from django.conf.urls import url
from game.api import views

urlpatterns = [
    url(
        regex=r'^(?P<pk>.+)/$',
        view=views.GameAPIView.as_view({'get': 'get',
                                        'patch': 'partial_update',
                                        'delete': 'retrieve'}),
        name='game_score_api'
    )
]

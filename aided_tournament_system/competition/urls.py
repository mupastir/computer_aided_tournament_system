from django.conf.urls import url

from .api import views

urlpatterns = [
    # /competition/
    url(
        regex=r'^detail/$',
        view=views.CompetitionListAPIView.as_view(),
        name='competition_rest_api'
    ),
    url(
        regex=r'^create/$',
        view=views.CompetitionCreateAPIView.as_view(),
        name='competition_create_rest_api'
    )
]

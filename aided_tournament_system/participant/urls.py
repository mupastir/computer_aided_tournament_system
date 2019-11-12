from django.conf.urls import url
from participant import views

urlpatterns = [
    url(
        regex=r'^add_player/$',
        view=views.PlayerCreateView.as_view(),
        name='add_player'
    ),
    url(
        regex=r'^add_referee/$',
        view=views.RefereeCreateView.as_view(),
        name='add_referee'
    ),
    url(
        regex=r'^ratings/$',
        view=views.ChoiceRatingView.as_view(),
        name='rating_choice'
    ),
    url(
        regex=r'^rating/(?P<type>.+)/(?P<gender>.+)/$',
        view=views.RatingView.as_view(),
        name='ratings'
    )
]

from competition import views
from django.conf.urls import url

urlpatterns = [
    url(
        regex=r'^competition_choice/$',
        view=views.CompetitionChoiceView.as_view(),
        name='competition_type_choice'
    ),
    url(
        regex=r'^create/$',
        view=views.CompetitionCreateView.as_view(),
        name='competition_create'
    ),
    url(
        regex=r'^(?P<competition_type>.+)/$',
        view=views.CompetitionFilteredView.as_view(),
        name='competition_filtered'
    ),
    url(
        regex=r'^(?P<competition_title>.+)/applications/$',
        view=views.CompetitionFilteredView.as_view(),
        name='applications'
    )
]

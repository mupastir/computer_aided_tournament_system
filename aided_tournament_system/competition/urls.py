from competition import views
from django.conf.urls import url

urlpatterns = [
    url(
        regex=r'^competition_choice/$',
        view=views.CompetitionChoiceView.as_view(),
        name='competition_type_choice'
    )
]

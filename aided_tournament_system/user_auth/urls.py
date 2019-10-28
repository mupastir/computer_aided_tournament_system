from django.conf.urls import url

from .api import views

urlpatterns = [
    # /user/
    url(
        regex=r'^$',
        view=views.UserReadAPIView.as_view(),
        name='user_rest_api',
    ),
]

from django.conf.urls import url
from user_auth import views

urlpatterns = [
    url(
        regex=r'^register/$',
        view=views.UserRegisterView.as_view(),
        name='user_register',
    ),
    url(
        regex=r'^<uuid:pk>/detail/$',
        view=views.UserInfoView.as_view(),
        name='user_register',
    ),
    url(
        regex=r'^login/$',
        view=views.UserLoginView.as_view(),
        name='user_register',
    ),
    url(
        regex=r'^logout/$',
        view=views.UserLogoutView.as_view(),
        name='user_register',
    )
]

from django.conf.urls import url
from user_auth import views

urlpatterns = [
    url(
        regex=r'^register/$',
        view=views.UserRegisterView.as_view(),
        name='user_register',
    ),
    url(
        regex=r'^update/(?P<pk>.+)/$',
        view=views.UserUpdateView.as_view(),
        name='user_update',
    ),
    url(
        regex=r'^detail/$',
        view=views.UserInfoView.as_view(),
        name='user_detail',
    ),
    url(
        regex=r'^login/$',
        view=views.UserLoginView.as_view(),
        name='user_login',
    ),
    url(
        regex=r'^logout/$',
        view=views.UserLogoutView.as_view(),
        name='user_logout',
    ),
    url(
        regex=r'^email/$',
        view=views.UserChangeEmailView.as_view(),
        name='user_email',
    ),
]

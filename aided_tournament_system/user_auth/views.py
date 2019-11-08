from allauth.account import views
from django.views.generic import DetailView
from user_auth.models import User


class UserInfoView(DetailView):
    model = User
    template_name = 'user_auth/detail.html'


class UserLoginView(views.LoginView):
    template_name = 'account/login.html'
    success_url = '/user/detail/'


class UserLogoutView(views.LogoutView):
    template_name = 'account/logout.html'
    success_url = '/user/detail/'


class UserRegisterView(views.SignupView):
    template_name = 'account/signup.html'
    success_url = '/user/detail/'

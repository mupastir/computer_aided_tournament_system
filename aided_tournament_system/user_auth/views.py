from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.instagram.views import InstagramOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import RegisterView, SocialLoginView, VerifyEmailView
from rest_auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from user_auth.models import User

from .serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = (IsAuthenticated,)


class UserLoginAPIView(LoginView):
    pass


class UserLogoutAPIView(LogoutView):
    pass


class UserRegisterAPIView(RegisterView):
    serializer_class = UserRegisterSerializer


class UserVerifyEmailAPIView(VerifyEmailView):
    pass


class UserPasswordResetAPIView(PasswordResetView):
    pass


class UserPasswordResetConfirmAPIView(PasswordResetConfirmView):
    pass


class UserPasswordChangeAPIView(PasswordChangeView):
    pass


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class InstagramLogin(SocialLoginView):
    adapter_class = InstagramOAuth2Adapter

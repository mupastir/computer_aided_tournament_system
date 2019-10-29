from aided_tournament_system.user_auth.models import User
from allauth.socialaccount.providers.facebook.views import \
    FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.instagram.views import \
    InstagramOAuth2Adapter
from rest_auth.registration.views import RegisterView, SocialConnectView
from rest_auth.views import LoginView, LogoutView
from rest_framework.generics import ListAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import (UserRegisterSerializer, UserSerializer,
                          UserUpdateSerializer)


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


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter


class GoogleConnect(SocialConnectView):
    adapter_class = GoogleOAuth2Adapter


class InstagramConnect(SocialConnectView):
    adapter_class = InstagramOAuth2Adapter

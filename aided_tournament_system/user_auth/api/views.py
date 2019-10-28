from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from ..models import User
from .serializers import UserCreateSerializer, UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer

from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from ..models import User
from .serializers import UserSerializer


class UserReadAPIView(ListAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

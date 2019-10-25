from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_swagger import renderers

from ..models import User
from .serializers import UserSerializer


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'uuid'

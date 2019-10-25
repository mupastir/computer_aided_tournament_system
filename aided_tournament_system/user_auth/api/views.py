from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from ..models import User
from .serializers import UserSerializer
from rest_framework_swagger import renderers


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    lookup_field = 'uuid'

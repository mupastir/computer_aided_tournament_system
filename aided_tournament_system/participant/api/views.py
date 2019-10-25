from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers

from ..models import Player, Team
from .serializers import PlayerSerializer, TeamSerializer


class PlayerLookAPIView(APIView):
    renderer_classes = [
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    ]
    permission_classes = (AllowAny,)

    def get(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)


class PlayerCreateAPIView(APIView):
    queryset = Player.objects.all()
    renderer_classes = (
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    )
    permission_classes = (AllowAny, )
    serializer_class = PlayerSerializer
    lookup_field = 'uuid'

    def post(self, request):
        generator = SchemaGenerator()
        schema = generator.get_schema(request=request)

        return Response(schema)


class TeamListCreateAPIView(APIView):
    queryset = Team.objects.all()
    renderer_classes = (
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    )
    permission_classes = (AllowAny,)
    serializer_class = TeamSerializer
    lookup_field = 'uuid'


class TeamRetrieveUpdateDestroyAPIView(APIView):
    queryset = Team.objects.all()
    renderer_classes = (
        renderers.OpenAPIRenderer,
        renderers.SwaggerUIRenderer
    )
    permission_classes = (IsAuthenticated, )
    serializer_class = TeamSerializer
    lookup_field = 'uuid'

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Aided tournament system API")

urlpatterns = [
    path("", schema_view),
    path("admin/", admin.site.urls),
    path("api/user/", include("user_auth.urls", namespace="api_user"), name="api_user"),
    path("api/competition/", include("competition.urls")),
    path("api/participant/", include("participant.urls")),
    path("api/game/", include("game.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Aided tournament system API')

urlpatterns = [
    path('', schema_view),
    path('admin/', admin.site.urls),
    path('api/user/', include('user_auth.api.urls'),
         name='api_user'),
    path('api/competition/', include('competition.api.urls')),
    path('api/participant/', include('participant.api.urls')),
    path('api/game/', include('game.api.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

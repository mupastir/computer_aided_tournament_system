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
from config import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Aided tournament system API')

urlpatterns = [
    path('', views.index, name='main'),
    path('admin/', admin.site.urls),
    path('api/user/', include('user_auth.api.urls')),
    path('api/competition/', include('competition.api.urls')),
    path('api/participant/', include('participant.api.urls')),
    path('api/game/', include('game.api.urls')),
    path('user/', include('user_auth.urls')),
    path('participant/', include('participant.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('swagger/', schema_view),
                      path('api-auth/', include('rest_framework.urls'),
                           name='rest_framework'),
                      path(r'rest-auth/', include('rest_auth.urls')),
                      path(r'accounts/', include('allauth.urls')),
                      path(r'rest-auth/registration/',
                           include('rest_auth.registration.urls')),
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

"""applicationTestApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.views.static import serve

# Create our schema's view w/ the get_schema_view() helper method. Pass in the proper Renderers for swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Candidates API",
        default_version='0.0.0'
    ),
    permission_classes=(permissions.IsAuthenticated, permissions.IsAdminUser)
)


class MainPageRedirectView(RedirectView):
    pattern_name = 'rest_framework:login'

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.pattern_name = 'schema-swagger-ui'
        return super().get_redirect_url(*args, **kwargs)


urlpatterns = [
    path("", MainPageRedirectView.as_view(), name='open-page'),
    path("drf-auth/", include('rest_framework.urls', namespace='rest_framework')),
    # DRF Doc Urls
    path("schema/", schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/signup/', include('rest_auth.registration.urls')),
    path('auth/refresh-token/', refresh_jwt_token),
    url(r'^attachments/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
    path("candidates/", include("applicationTestApi.candidate.urls", namespace='Candidates')),
    path("users/", include("applicationTestApi.users.urls", namespace='Users')),
]

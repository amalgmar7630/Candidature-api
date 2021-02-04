from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from applicationTestApi.users.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'', UserViewSet)

app_name = "users"

urlpatterns = [
    url(r'^', include(router.urls)),
]
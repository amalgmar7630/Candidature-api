from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from applicationTestApi.candidate.viewsets import CandidateViewSet

router = routers.DefaultRouter()
router.register(r'', CandidateViewSet)

app_name = "candidate"

urlpatterns = [
    url(r'^', include(router.urls)),
]
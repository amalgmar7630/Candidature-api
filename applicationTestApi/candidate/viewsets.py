from django.core.mail import send_mail
from rest_framework import viewsets

from applicationTestApi.candidate.models import Candidate
from applicationTestApi.candidate.serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        print('create')
        super(CandidateViewSet, self).perform_create(serializer)
        email = serializer.validated_data.pop('email')
        k = send_mail(
            'Application Sent successfully',
            'Your application is saved successfully',
            'info@test.com',
            [email],
            fail_silently=False,
        )
        serializer.save()

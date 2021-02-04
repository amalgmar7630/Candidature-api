from rest_framework import serializers

from applicationTestApi.candidate.models import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('id', 'firstname', 'lastname', 'email', 'birthdate', 'phone', 'availability', 'years_experience', 'cv_file', 'message', 'application_status',)

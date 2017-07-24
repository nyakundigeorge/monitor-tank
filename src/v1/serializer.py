from rest_framework import serializers
from v1.models import Report, Suscriber

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['context']

class SuscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriber
        fields = ['subscriber_number', 'access_token']

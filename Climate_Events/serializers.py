from rest_framework import serializers
from .models import ClimateEvent

class ClimateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateEvent
        fields = ['id', 'event_title', 'location', 'description', 'image', 'event_date', 'event_time']

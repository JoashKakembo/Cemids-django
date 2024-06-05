from django.shortcuts import render
from rest_framework import viewsets
from .models import ClimateEvent
from .serializers import ClimateEventSerializer

class ClimateEventViewSet(viewsets.ModelViewSet):
    queryset = ClimateEvent.objects.all()
    serializer_class = ClimateEventSerializer

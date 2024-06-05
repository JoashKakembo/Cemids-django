from django.shortcuts import render
from rest_framework import viewsets
from .models import ProfileSettings
from .serializers import ProfileSettingsSerializer

class ProfileSettingsViewSet(viewsets.ModelViewSet):
    queryset = ProfileSettings.objects.all()
    serializer_class = ProfileSettingsSerializer


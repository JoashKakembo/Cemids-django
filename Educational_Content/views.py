from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EducationalContentSerializer
from .models import EducationalContent

# Create your views here.

class EducationalContentView(viewsets.ModelViewSet):
    serializer_class = EducationalContentSerializer
    queryset = EducationalContent.objects.all()

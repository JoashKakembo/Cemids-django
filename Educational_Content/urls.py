from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationalContentView

router = DefaultRouter()
router.register(r'Educational_Content', EducationalContentView)

urlpatterns = [
    path('', include(router.urls)),
]

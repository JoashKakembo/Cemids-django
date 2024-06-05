from django.urls import path, include
from rest_framework import routers
from .views import ProfileSettingsViewSet

router = routers.DefaultRouter()
router.register(r'profile_settings', ProfileSettingsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

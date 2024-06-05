from django.urls import path, include
from rest_framework import routers
from .views import DonationView

router = routers.DefaultRouter()
router.register(r'Donation', DonationView, 'Donation')


urlpatterns = [
    path('', include(router.urls)),
]
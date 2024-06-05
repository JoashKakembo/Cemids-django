from django.contrib import admin
from django.urls import include
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Climate_Events.urls')),
    path('api/', include('Donation.urls')),
    path('api/', include('Educational_Content.urls')),  
     path('api/', include('profile_settings.urls')),  
]


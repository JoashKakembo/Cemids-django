from rest_framework import serializers
from .models import ProfileSettings

class ProfileSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileSettings
        fields = ['id', 'profile_photo', 'first_name', 'surname', 'email', 'phonenumber', 'gender', 'nationality', 'date_of_birth', 'job_title']

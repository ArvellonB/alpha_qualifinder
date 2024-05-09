# In users/serializers.py
from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user', 'headline', 'summary', 'location', 'profile_picture_url']  # Ensure 'headline' is here

    def to_representation(self, instance):
        """Customize output if necessary."""
        ret = super().to_representation(instance)
        return ret

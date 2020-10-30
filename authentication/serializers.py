from .models import Profile
from rest_framework import serializers

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=['id','name','image','get_absolute_url']
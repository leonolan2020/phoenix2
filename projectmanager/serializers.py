from rest_framework import serializers 
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project        
        fields=['get_link']
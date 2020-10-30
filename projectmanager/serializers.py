from rest_framework import serializers 
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project        
        fields=['get_link']
class ContractorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contractor        
        fields=['get_link']
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event        
        fields=['id','title','get_tag','short_description','persian_date_added']
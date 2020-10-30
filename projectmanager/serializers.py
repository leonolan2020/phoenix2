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
        fields=['get_tag']
class ArchiveDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['get_link']
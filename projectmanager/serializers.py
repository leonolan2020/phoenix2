from rest_framework import serializers 
from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project        
        fields=['id','parent','get_resource','get_link','start_date','end_date','persian_start_date','persian_end_date','title','percent']
class ContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contractor        
        fields=['id','color','get_link','title','get_absolute_url']
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event        
        fields=['get_tag']

class OrganiazationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganiazationUnit        
        fields=['id','title','parent_title','caption']
class ArchiveDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['get_link']
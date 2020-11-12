from rest_framework import serializers 
from .models import *
from authentication.serializers import ProfileSerializer

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Project        
        fields=['id','parent','color','get_absolute_url','get_resource','get_link','start_date','end_date','persian_start_date','persian_end_date','title','percent']
class ContractorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Contractor        
        fields=['id','color','get_link','title','get_absolute_url']
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event        
        fields=['get_tag']
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model=Material        
        fields=['id','title','short_description','thumbnail','get_absolute_url','get_edit_url','unit_name']

class MaterialObjectSerializer(serializers.ModelSerializer):
    material=MaterialSerializer()
    class Meta:
        model=MaterialObject        
        fields=['id','material','serial_no']

class MaterialRequestSignatureSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=MaterialRequestSignature        
        fields=['id','profile','status','description','persian_date_added','get_status_color']
class MaterialRequestSerializer(serializers.ModelSerializer):
    material=MaterialSerializer()
    profile=ProfileSerializer()
    project=ProjectSerializer()
    class Meta:
        model=MaterialRequest      
        fields=['id','material','profile','project','get_absolute_url','get_edit_url','get_status_tag','quantity','persian_date_added','persian_date_delivered']
class MaterialWareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=MaterialWareHouse        
        fields=['id','get_link']
        
class MaterialInStockSerializer(serializers.ModelSerializer):
    material_object=MaterialObjectSerializer()
    class Meta:
        model=MaterialInStock        
        fields=['id','material_object','row','col']
class EmployeeSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=Employee        
        fields=['id','role','get_absolute_url','profile']

class OrganizationUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrganizationUnit        
        fields=['id','title','employees_caption','get_link','parent_id','parent_title','caption']
class ArchiveDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['get_link']
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=ArchiveDocument        
        fields=['color','get_absolute_url','title','id']
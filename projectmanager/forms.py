from django import forms
from django.shortcuts import reverse
from .apps import APP_NAME
from dashboard.settings import SITE_URL
class AddMaterialRequestForm(forms.Form):
    material_id=forms.IntegerField(required=True)
    quantity=forms.IntegerField(required=True)
    unit_name=forms.CharField(max_length=50, required=True)
    project_id=forms.IntegerField(required=True)

class AddEmployeeForm(forms.Form):
    first_name=forms.CharField(max_length=50,required=True)
    last_name=forms.CharField(max_length=50,required=True)
    role=forms.CharField(max_length=50,required=True)
    org_unit_id=forms.IntegerField(required=True)
    
class AddMaterialForm(forms.Form):
    title=forms.CharField(max_length=50,required=True)
    category_id=forms.IntegerField(required=True)
class AddMaterialCategoryForm(forms.Form):
    title=forms.CharField(max_length=50,required=True)
    parent_id=forms.IntegerField(required=True)

class DoSignatureForm(forms.Form):
    description=forms.CharField(max_length=500,required=True)
    status=forms.CharField(max_length=50,required=True)
    materialrequest_id=forms.IntegerField(required=True)
    
class AddOrganizationUnitForm(forms.Form):
    title=forms.CharField(max_length=50,required=True)
    parent_id=forms.IntegerField(required=True)
class SearchForm(forms.Form):
    action=f'{SITE_URL}{APP_NAME}/search/'
    search_for=forms.CharField(max_length=50, required=True)

class AddProjectForm(forms.Form):
    parent_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)

class AddMaterialWareHouseForm(forms.Form):
    parent_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)

class AddContractorForm(forms.Form):
    title=forms.CharField(max_length=100,required=True)

class AddArchiveDocumentForm(forms.Form):
    parent_id=forms.IntegerField(required=False)
    category_id=forms.IntegerField(required=False)
    title=forms.CharField(max_length=100,required=True)

class AddArchiveCategoryForm(forms.Form):
    parent_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)

class AddAssignmentForm(forms.Form):
    project_id=forms.IntegerField(required=True)
    employee_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100, required=True)
    status=forms.CharField(max_length=100, required=True)

class AddLocationForm(forms.Form):
    page_id=forms.IntegerField(required=True)
    location=forms.CharField(max_length=500,required=True)

class AddEventForm(forms.Form):
    project_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=200,required=True)
    short_description=forms.CharField(max_length=500,required=True)
    event_date=forms.CharField(max_length=20,required=True)

class EditProjectTimingForm(forms.Form):
    project_id=forms.IntegerField(required=True)
    start_date=forms.CharField(max_length=50,required=True)
    end_date=forms.CharField(max_length=50,required=True)
    percent=forms.IntegerField(required=True)
class AddWorkUnitForm(forms.Form):
    parent_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=50,required=True)

class AddIssueForm(forms.Form):
    page_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)
    issue_type=forms.CharField(max_length=50,required=True)
    

class SignMaterialRequestForm(forms.Form):
    material_request_id=forms.IntegerField(required=True)
    status=forms.CharField(max_length=50, required=True)
    description=forms.CharField(max_length=500, required=False)

class PriorityForm(forms.Form):
    pk=forms.CharField(max_length=50, required=True)
    direction=forms.CharField(max_length=5, required=True)
    base_class=forms.CharField(max_length=20,required=True)
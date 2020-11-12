
from rest_framework.views import APIView
from .repo import *
from .serializers import *
from .forms import *
from django.http import JsonResponse

class PageViews(APIView):
    def add_project(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                log=3
                title=add_project_form.cleaned_data['title']
                parent_id=add_project_form.cleaned_data['parent_id']
                project=ProjectRepo(user=user).add(title=title,parent_id=parent_id)
                if project is not None:
                    log=4
                    project_s=ProjectSerializer(project).data
                    return JsonResponse({'result':SUCCEED,'project':project_s})
        return JsonResponse({'result':FAILED,'log':log})
    def add_document(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_document_form=AddArchiveDocumentForm(request.POST)
            if add_document_form.is_valid():
                log=3
                title=add_document_form.cleaned_data['title']
                parent_id=add_document_form.cleaned_data['parent_id']
                document=ArchiveDocumentRepo(user=user).add(title=title,parent_id=parent_id)
                if document is not None:
                    log=4
                    document_s=ArchiveDocumentSerializer(document).data
                    return JsonResponse({'result':SUCCEED,'document':document_s})
        return JsonResponse({'result':FAILED,'log':log})
    def add_location(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_location_form=AddLocationForm(request.POST)
            if add_location_form.is_valid():
                log=3
                location=add_location_form.cleaned_data['location']
                project_id=add_location_form.cleaned_data['page_id']
                location=location.replace('width="600"','width="100%"')
                location=location.replace('height="450"','height="400"')                    
                # project=ProjectRepo(user=user).project(project_id=project_id)
                project=ProjectRepo(user=user).edit_location(project_id=project_id,location=location)
                if project is not None:
                    log=4                    
                    return JsonResponse({'result':SUCCEED,'location':location})
        return JsonResponse({'result':FAILED,'log':log})
    def add_materialwarehouse(self,request):
        user=request.user
        if request.method=='POST':
            add_materialwarehouse_form=AddMaterialWareHouseForm(request.POST)
            if add_materialwarehouse_form.is_valid():
                title=add_materialwarehouse_form.cleaned_data['title']
                parent_id=add_materialwarehouse_form.cleaned_data['parent_id']
                materialwarehouse=MaterialWareHouseRepo(user=user).add(title=title,parent_id=parent_id)
                if materialwarehouse is not None:
                    materialwarehouse_s=MaterialWareHouseSerializer(materialwarehouse).data
                    return JsonResponse({'result':SUCCEED,'materialwarehouse':materialwarehouse_s})
    def add_contractor(self,request):
        user=request.user
        if request.method=='POST':
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                title=add_project_form.cleaned_data['title']
                contractor=ContractorRepo(user=user).add(title=title)
                if contractor is not None:
                    contractor_s=ContractorSerializer(contractor).data
                    return JsonResponse({'result':SUCCEED,'contractor':contractor_s})
    def add_event(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_event_form=AddEventForm(request.POST)
            if add_event_form.is_valid():
                log=3
                project_id=add_event_form.cleaned_data['project_id']
                title=add_event_form.cleaned_data['title']
                short_description=add_event_form.cleaned_data['short_description']
                event_date=add_event_form.cleaned_data['event_date']
                project=ProjectRepo(user=request.user).project(project_id=project_id)
                event_date=PersianCalendar().to_gregorian(event_date)
                if project is not None:
                    log=4
                    event=EventRepo(user=user).add(project_id=project_id,title=title,short_description=short_description,event_date=event_date)
                    if event is not None:
                        log=5
                        events_s=EventSerializer(project.events.order_by('-event_date'),many=True).data
                        return JsonResponse({'result':SUCCEED,'events':events_s})
        return JsonResponse({'result':FAILED,'log':log})
    def edit_project_timing(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            edit_project_timing_form=EditProjectTimingForm(request.POST)
            if edit_project_timing_form.is_valid():
                log=3
                project_id=edit_project_timing_form.cleaned_data['project_id']
                start_date=edit_project_timing_form.cleaned_data['start_date']
                end_date=edit_project_timing_form.cleaned_data['end_date']
                percent=edit_project_timing_form.cleaned_data['percent']

                project=ProjectRepo(user=request.user).project(project_id=project_id)
                start_date=PersianCalendar().to_gregorian(start_date)
                end_date=PersianCalendar().to_gregorian(end_date)
                if project is not None:
                    log=4
                    project=ProjectRepo(user=user).edit_timing(project_id=project_id,start_date=start_date,end_date=end_date,percent=percent)
                    if project is not None:
                        log=5
                        EventSerializer(project.events.order_by('-event_date'),many=True).data
                        return JsonResponse({'result':SUCCEED,'start_date':project.persian_start_date(),'percent':project.percent,'end_date':project.persian_end_date()})
        return JsonResponse({'result':FAILED,'log':log})
    def add_organizationunit(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_organizationunit_form=AddOrganizationUnitForm(request.POST)
            if add_organizationunit_form.is_valid():
                log=3
                title=add_organizationunit_form.cleaned_data['title']
                parent_id=add_organizationunit_form.cleaned_data['parent_id']
                organizationunit=OrganizationUnitRepo(user=user).add(title=title,parent_id=parent_id)
                if organizationunit is not None:
                    log=4
                    organizationunit_s=OrganizationUnitSerializer(organizationunit).data
                    return JsonResponse({'result':SUCCEED,'organizationunit':organizationunit_s})
        return JsonResponse({'result':FAILED,'log':log})
    def add_employee(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            add_employee_form=AddEmployeeForm(request.POST)
            if add_employee_form.is_valid():
                log=3
                first_name=add_employee_form.cleaned_data['first_name']
                last_name=add_employee_form.cleaned_data['last_name']
                org_unit_id=add_employee_form.cleaned_data['org_unit_id']
                role=add_employee_form.cleaned_data['role']


                employee=EmployeeRepo(user=user).add(role=role,org_unit_id=org_unit_id,first_name=first_name,last_name=last_name,)
                if employee is not None:
                    log=4
                    employee_s=EmployeeSerializer(employee).data
                    return JsonResponse({'result':SUCCEED,'employee':employee_s})
        return JsonResponse({'result':FAILED,'log':log})
    def do_signature(self,request):
        log=1
        user=request.user
        if request.method=='POST':
            log=2
            do_signature_form=DoSignatureForm(request.POST)
            if do_signature_form.is_valid():
                log=3
                materialrequest_id=do_signature_form.cleaned_data['materialrequest_id']
                description=do_signature_form.cleaned_data['description']
                status=do_signature_form.cleaned_data['status']


                signature=MaterialRequestRepo(user=user).do_signature(status=status,description=description,materialrequest_id=materialrequest_id)
                if signature is not None:
                    log=4
                    signature_s=MaterialRequestSignatureSerializer(signature).data
                    return JsonResponse({'result':SUCCEED,'signature':signature_s})
        return JsonResponse({'result':FAILED,'log':log})
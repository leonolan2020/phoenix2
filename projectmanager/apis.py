
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
                project=ProjectRepo(user=user).project(project_id=project_id)
                if project is not None:
                    log=4
                    location=location.replace('width="600"','width="100%"')
                    location=location.replace('height="450"','height="400"')
                    project.location=location
                    project.save()
                    return JsonResponse({'result':SUCCEED,'location':location})
        return JsonResponse({'result':FAILED,'log':log})
    def add_contractor(self,request):
        user=request.user
        if request.method=='POST':
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                title=add_project_form.cleaned_data['title']
                contractor=ContractorRepo(user=user).add(title=title)
                if contractor is not None:
                    contractor_s=ContractorSerializer(contractor).data
                    return JsonResponse(contractor_s)
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
                    event=EventRepo(user=user).add(project_id=project_id,title=title,short_description=short_description,date_added=event_date)
                    if event is not None:
                        log=5
                        events_s=EventSerializer(project.events.all(),many=True).data
                        return JsonResponse({'result':SUCCEED,'events':events_s})
        return JsonResponse({'result':FAILED,'log':log})

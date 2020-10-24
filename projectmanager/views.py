from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
from .repo import *
from .serializers import *
from .forms import *
import json

TEMPLATE_ROOT='projectmanager/'
def getContext(request):
    user=request.user
    context=DashboardContext(request)
    return context

class BasicViews(View):
    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        projects=ProjectRepo(user=user).list_roots()
        context['projects']=projects
        context['add_project_form']=AddProjectForm()
        return render(request,TEMPLATE_ROOT+'index.html',context)

class ApiViews(View):
    def add_project(self,request):
        user=request.user
        if request.method=='POST':
            add_project_form=AddProjectForm(request.POST)
            if add_project_form.is_valid():
                title=add_project_form.cleaned_data['title']
                parent_id=add_project_form.cleaned_data['parent_id']
                project=ProjectRepo(user=user).add(title=title,parent_id=parent_id)
                if project is not None:
                    project_s=ProjectSerializer(project).data
                    return JsonResponse(project_s)
class PageViews(View):
    def project(self,request,pk,*args, **kwargs):
        project_id=pk
        user=request.user
        context=getContext(request)
        project=ProjectRepo(user=user).project(project_id=project_id)
        context['project']=project
        context['page']=project
        return render(request,TEMPLATE_ROOT+'project.html',context)



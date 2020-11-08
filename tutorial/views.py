from django.shortcuts import render,reverse,redirect
from dashboard.views import getContext as DashboardContext
from django.http import Http404
from django.views import View
from .apps import APP_NAME
TEMPLATE_ROOT='tutorial/'
PROJECT_MANAGER='projectmanager/'
def getContext(request):
    context=DashboardContext(request)
    context['app']={
        'title':'tutorial'
    }
    return context
class BasicViews(View):
    def home(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)

class ProjectManagerTutorials(View):
    def add_project_location(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+PROJECT_MANAGER+'add-project-location.html',context)
    
from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
from .repo import ProjectRepo
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
        projects=ProjectRepo(user=user).list()
        context['projects']=projects
        return render(request,TEMPLATE_ROOT+'index.html',context)


# Create your views here.

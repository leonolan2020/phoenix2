from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
import json

TEMPLATE_ROOT='projectmanager/'
def getContext(request):
    context=DashboardContext(request)
    return context

class BasicViews(View):
    def home(self,request,*args, **kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)


# Create your views here.

from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from .forms import *
from authentication.repo import ProfileRepo

TEMPLATE_ROOT='material/'




def getContext(request):
    context={}
    context['title']="فونیکس"
    context['ADMIN_URL']=ADMIN_URL
    context['MEDIA_URL']=MEDIA_URL
    context['dashboard']={
        'pretitle':'دشبورد',
        'title':'آموزشگاه'
    }
    context['profile']=ProfileRepo(user=request.user).me
    return context

class BasicViews(View):
    def home(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)




# Create your views here.

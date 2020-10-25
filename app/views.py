from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL,MEDIA_URL
from dashboard.repo import *
from .forms import *
from authentication.repo import ProfileRepo
from dashboard.views import getContext as DashboardContext

TEMPLATE_ROOT='material/'




def getContext(request):
    context=DashboardContext(request)
    return context

class BasicViews(View):
    def home(self,request,*args,**kwargs):
        user=request.user
        context=getContext(request)
        homesliders=HomeSliderRepo(user=user).list()
        context['homesliders']=homesliders
        features=FeatureRepo(user=user).list_for_home()
        context['features']=features
        blogs=BlogRepo(user=user).list_for_home()
        context['blogs']=blogs
        ourworks=OurWorkRepo(user=user).list_for_home()
        context['ourworks']=ourworks
        ourteams=OurTeamRepo(user=user).list()
        context['ourteams']=ourteams
        return render(request,TEMPLATE_ROOT+'index.html',context)

    def features(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'features.html',context)

class ProfileViews(View):
    def profile(self,request,profile_id=0,*args,**kwargs):
        if profile_id==0:
            selected_profile=ProfileRepo(user=request.user).me
        else:
            selected_profile=ProfileRepo(user=request.user).get(profile_id=profile_id)
        context=getContext(request)
        context['body_class']='profile-page'
        context['selected_profile']=selected_profile
        return render(request,TEMPLATE_ROOT+'profile.html',context)

class ExampleViews(View):
    def all_components(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/all-components.html',context)
    def sections(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/sections.html',context)


class PageViews(View):
    def blog(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'blog.html',context)
    def feature(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)
    def ourwork(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'index.html',context)

# Create your views here.

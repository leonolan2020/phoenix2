from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from dashboard.enums import *
from .forms import *
from authentication.repo import ProfileRepo
from dashboard.views import getContext as DashboardContext
from dashboard.utils import AdminUtility
TEMPLATE_ROOT='material/'




def getContext(request):
    user=request.user
    context=DashboardContext(request)
    context['admin_utility']=AdminUtility(app_name=APP_NAME)
    return context

class BasicViews(View):
    def contact(self,request,*args, **kwargs):
        context=getContext(request)
        context['body_class']='contact-page'
        return render(request,TEMPLATE_ROOT+'contact.html',context)

    def about(self,request,*args, **kwargs):
        context=getContext(request)
        user=request.user
        context['body_class']='about-us'
        context['about_header']=MainPicRepo(user=user).get(MainPicEnum.ABOUT_HEADER)
        context['about_text']=ParameterRepo(user=user).get(ParametersEnum.ABOUT_US_TITLE)
        return render(request,TEMPLATE_ROOT+'about.html',context)

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
    def get_page_context(self,request,pk,page_type,*args, **kwargs):
        pass

    def resume(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        resume=ResumeRepo(user=user).resume(resume_id=pk)
        context['page']=resume
        context['resume']=resume
        return render(request,TEMPLATE_ROOT+'resume.html',context)
    def blog(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        blog=BlogRepo(user=user).blog(blog_id=pk)
        context['page']=blog
        context['blog']=blog
        return render(request,TEMPLATE_ROOT+'blog.html',context)
    def feature(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        feature=FeatureRepo(user=user).feature(feature_id=pk)
        context['page']=feature
        context['feature']=feature
        return render(request,TEMPLATE_ROOT+'feature.html',context)
    def ourwork(self,request,pk,*args, **kwargs):
        user=request.user
        context=getContext(request)
        ourwork=OurWorkRepo(user=user).ourwork(ourwork_id=pk)
        context['page']=ourwork
        context['ourwork']=ourwork
        return render(request,TEMPLATE_ROOT+'ourwork.html',context)

# Create your views here.

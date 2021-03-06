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
TEMPLATE_ROOT='material_en/'




def getContext(request):
    user=request.user
    context=DashboardContext(request)
    parameter_repo=ParameterRepo(user=request.user)
    main_pic_repo=MainPicRepo(user=request.user)
    link_repo=LinkRepo(user=request.user)
    context['app']={
        'theme_color':parameter_repo.get(ParametersEnum.THEME_COLOR),
        'nav_items':link_repo.get_nav_items(),
        'about_us_short':parameter_repo.get(ParametersEnum.ABOUT_US_SHORT),
        'GOOGLE_SEARCH_CONSOLE_TAG':parameter_repo.get(ParametersEnum.GOOGLE_SEARCH_CONSOLE_TAG),
        'NAV_TEXT_COLOR':parameter_repo.get(ParametersEnum.NAV_TEXT_COLOR),
        'NAV_BACK_COLOR':parameter_repo.get(ParametersEnum.NAV_BACK_COLOR),
        'slogan':parameter_repo.get(ParametersEnum.SLOGAN),
        'logo':main_pic_repo.get(name=MainPicEnum.LOGO),
        'favicon':main_pic_repo.get(name=MainPicEnum.FAVICON),
        'loading':main_pic_repo.get(name=MainPicEnum.LOADING),
        'pretitle':parameter_repo.get(ParametersEnum.PRE_TILTE),
        'title':parameter_repo.get(ParametersEnum.TITLE),
        'address':parameter_repo.get(ParametersEnum.ADDRESS),    
        'mobile':parameter_repo.get(ParametersEnum.MOBILE),           
        'email':parameter_repo.get(ParametersEnum.EMAIL),      
        'tel':parameter_repo.get(ParametersEnum.TEL),
        'url':parameter_repo.get(ParametersEnum.URL),
        'meta_data_items':MetaDataRepo().list_for_home(),
        'our_team_title':OurTeamRepo(user=user).get_title(),
        'our_team_link':OurTeamRepo(user=user).get_link(),
    }
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

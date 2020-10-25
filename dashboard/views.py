from django.shortcuts import render
from django.views import View
from .settings import *
from .repo import *
from .forms import *
from .enums import *
from .settings import DEBUG
from .serializers import * #NotificationSerializer
if PUSHER_IS_ENABLE:
    from leopusher.repo import PusherChannelEventRepo
    from leopusher.serializers import PusherChannelEventSerializer

import json
from authentication.repo import ProfileRepo
TEMPLATE_ROOT='dashboard/'

def getContext(request):
    user=request.user
    context={}
    context['title']="فونیکس"
    context['DEBUG']=DEBUG
    context['ADMIN_URL']=ADMIN_URL
    context['MEDIA_URL']=MEDIA_URL
    context['SITE_URL']=SITE_URL
    context['PUSHER_IS_ENABLE']=PUSHER_IS_ENABLE
    if user.is_authenticated:
        profile=ProfileRepo(user=user).me    
        context['profile']=profile 
        context['notifications_s']=json.dumps(NotificationSerializer(NotificationRepo(user=request.user).list_unseen(),many=True).data)
        context['notifications_count']=NotificationRepo(user=user).count
        profiles=ProfileRepo(user=user).list_by_user(user=user)
        if profile is not None:
            context['profiles']=profiles.exclude(pk=profile.pk)
        if PUSHER_IS_ENABLE:            
            my_channel_events=PusherChannelEventRepo(user=user).my_channel_events()
            my_channel_events_s=PusherChannelEventSerializer(my_channel_events,many=True).data
            context['my_channel_events_s']=json.dumps(my_channel_events_s)
    else:
        context['profile']=None                
        context['profiles']=None            
        context['my_channel_events_s']='[]'
        context['notifications_s']='[]'
    parameter_repo=ParameterRepo(user=request.user)
    main_pic_repo=MainPicRepo(user=request.user)
    link_repo=LinkRepo(user=request.user)
    context['app']={
        'nav_items':link_repo.get_nav_items(),
        'about_us_short':parameter_repo.get(ParametersEnum.ABOUT_US_SHORT),
        'GOOGLE_SEARCH_CONSOLE_TAG':parameter_repo.get(ParametersEnum.GOOGLE_SEARCH_CONSOLE_TAG),
        'NAV_TEXT_COLOR':parameter_repo.get(ParametersEnum.NAV_TEXT_COLOR),
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

    context['profile']=ProfileRepo(user=request.user).me
    return context



class BasicViews(View):
    def home(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'dashboard.html',context)
    def charts(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'charts.html',context)
    def wizard(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'wizard.html',context)
    def widgets(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'widgets.html',context)
    def calendar(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'calendar.html',context)

class PagesViews(View):
    def timeline(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'pages/timeline.html',context)
class TablesViews(View):
    def regular(self,request,*args,**kwargs):
        context=getContext(request)
        notifications=NotificationRepo(user=request.user).list_all()
        context['notifications']=notifications
        return render(request,TEMPLATE_ROOT+'tables/regular.html',context)
    
class ComponentsViews(View):
    def buttons(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/buttons.html',context)
    def panels(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/panels.html',context)
    def notifications(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/notifications.html',context)
    def alerts(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/alerts.html',context)

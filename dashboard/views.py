from django.shortcuts import render
from django.views import View
from .settings import ADMIN_URL
TEMPLATE_ROOT='dashboard/'

def getContext(request):
    context={}
    context['title']="فونیکس"
    context['ADMIN_URL']=ADMIN_URL
    context['dasboard_title']="دشبورد فونیکس"
    return context

class AuthenticationView(View):
    def login(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,'auth/login.html',context)




class BasicView(View):
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

class PagesView(View):
    def timeline(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'pages/timeline.html',context)
class TablesView(View):
    def regular(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'tables/regular.html',context)
    
class ComponentsView(View):
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

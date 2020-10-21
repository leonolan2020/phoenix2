from django.shortcuts import render
from django.views import View
TEMPLATE_ROOT='dashboard/'

def getContext(request):
    context={}
    context['title']="فونیکس"
    context['dasboard_title']="دشبورد فونیکس"
    return context

class BasicView(View):
    def home(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'dashboard.html',context)

class PagesView(View):
    def timeline(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'pages/timeline.html',context)

class ComponentsView(View):
    def buttons(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/buttons.html',context)
    def panels(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/panels.html',context)
    def alerts(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'components/alerts.html',context)

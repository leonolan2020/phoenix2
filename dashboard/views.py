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
    def timeline(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'timeline.html',context)
# Create your views here.

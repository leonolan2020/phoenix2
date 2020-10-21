from django.shortcuts import render
from django.views import View
TEMPLATE_ROOT='dashboard/'

def getContext(request):
    context={}
    context['title']="material dashboard"
    return context

class BasicView(View):
    def home(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'dashboard.html',context)
# Create your views here.

from django.shortcuts import render,redirect,reverse
from django.views import View
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from .forms import *
from .repo import ProfileRepo
TEMPLATE_ROOT='authentication/'
# Create your views here.
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

class AuthenticationView(View):
    def login(self,request,*args,**kwargs):
        if request.method=='POST':
            return self.login_post(request)
        else:
            context=getContext(request)
            context['login_form']=LoginForm()
            return render(request,TEMPLATE_ROOT+'login.html',context)

    def logout(self,request):
        ProfileRepo().logout(request)
        return redirect(reverse('dashboard:home'))

    def login_post(self,request,back_url=None,next1=None):
        back_url=request.GET.get('next1', '')
        if back_url is None or not back_url:
            # back_url=reverse('app:my_profile')
            back_url=reverse('dashboard:home')
        if request.method=='POST':
            login_form=LoginForm(request.POST)
            if login_form.is_valid():
                username=login_form.cleaned_data['username']
                password=login_form.cleaned_data['password']                
                request1=ProfileRepo().login(request=request,username=username,password=password)
                if request1 is not None and request1.user is not None and request1.user.is_authenticated :
                    return redirect(back_url)
                else:   
                    context=getContext(request=request)         
                    context['message']='نام کاربری و کلمه عبور صحیح نمی باشد'
                    context['login_form']=LoginForm()
                    context['register_form']=RegisterForm()
                    context['reset_password_form']=ResetPasswordForm()
                    return render(request,TEMPLATE_ROOT+'login.html',context)
        else:      
            return redirect(reverse('authentication:login'))
from django.shortcuts import render,redirect,reverse
from django.views import View
from django.http import JsonResponse,Http404
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .repo import *
from .forms import *
from dashboard.constants import SUCCEED,FAILED
from .repo import ProfileRepo
from dashboard.views import getContext as DashboardContext

TEMPLATE_ROOT='authentication/'
# Create your views here.
def getContext(request):
    context=DashboardContext(request)

    return context

class AuthenticationView(View):
    def edit_profile(self,request,*args,**kwargs):
        if request.method=='POST':
            edit_profile_form=EditProfileForm(request.POST)
            if edit_profile_form.is_valid():
                profile_id=edit_profile_form.cleaned_data['profile_id']
                first_name=edit_profile_form.cleaned_data['first_name']
                last_name=edit_profile_form.cleaned_data['last_name']
                mobile=edit_profile_form.cleaned_data['mobile']
                slogan=edit_profile_form.cleaned_data['slogan']
                bio=edit_profile_form.cleaned_data['bio']
                address=edit_profile_form.cleaned_data['address']
                postal_code=edit_profile_form.cleaned_data['postal_code']
                edited_profile=ProfileRepo(user=request.user).edit_profile(
                    profile_id=profile_id,
                    first_name=first_name,
                    last_name=last_name,
                    mobile=mobile,
                    slogan=slogan,
                    bio=bio,
                    address=address,
                    postal_code=postal_code
                    )
                if edited_profile is not None:
                    return JsonResponse({'result':SUCCEED})
        return JsonResponse({'result':FAILED})
    def profile(self,request,profile_id=0,*args,**kwargs):
        if profile_id==0:
            selected_profile=ProfileRepo(user=request.user).me
        else:
            selected_profile=ProfileRepo(user=request.user).get(profile_id=profile_id)

        context=getContext(request)
        context['login_form']=LoginForm()
        context['selected_profile']=selected_profile
        return render(request,TEMPLATE_ROOT+'profile.html',context)
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
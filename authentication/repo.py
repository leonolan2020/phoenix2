from django.contrib.auth import login, logout, authenticate
from .models import Profile
from .enums import ProfileStatusEnum
from django.contrib.auth.models import User
from .apps import APP_NAME

from django.contrib.auth.models import Permission



class ProfileRepo:    
    def search(self,search_for):
        return self.objects.filter(Q(first_name__contains=search_for) | Q(last_name__contains=search_for))

    def __init__(self,user=None):
        if user is not None and user and user.is_authenticated:

            self.user = user
            self.objects = Profile.objects.filter(status=ProfileStatusEnum.ENABLED)
            try:
                self.me = self.objects.filter(user=user).filter(selected=True)[0]          
            except :
                profiles = self.objects.filter(user=user)
                if len(profiles)>0:
                    for profile in profiles:
                        profile.selected=False
                        profile.save()
                    profiles[0].selected=True
                    profiles[0].save()
                    self.me= profiles[0]
                else:
                    self.me=None
                    
        else:
            self.me=None
            self.objects=None
            self.user=None          
        
    def list_all(self):
        if self.user is not None and self.user.is_authenticated:
            return self.objects.all()
    
    def reset_selected_profile(self,user):
        profiles=self.objects.filter(user=user)
        if len(profiles)>0:
            for profile in profiles:
                profile.selected=False
                profile.save()
            profiles[0].selected=True
            profiles[0].save()
            return profiles[0]
        return None
  
    def get_by_user(self,user):
        if user is None or not user.is_authenticated:
            return None
        try:
            profile = self.objects.filter(user=user).filter(selected=True)[0]           
            return profile
        except :
            return self.reset_selected_profile(user=user)
    
    def list_by_user(self,user):
        profiles=self.objects.filter(user=user)
        return profiles
    
    def change_profile(self,user,actived):
        try:
            profile1=self.objects.filter(user=user).get(pk=actived)
            
            profiles=self.objects.filter(user=user)
            for profile in profiles:
                profile.selected=False
                profile.save()
            profile1.selected=True
            profile1.save()
            return profile1
        except:
            pass
        return None
    
    def change_profile_image(self,profile_id,image):
        profile=ProfileRepo(user=self.user).get(profile_id=profile_id)
        if profile is not None:
            profile.image_origin = image
            profile.save()
            return True
        return False
    
    def edit_profile(self,profile_id,first_name,last_name,mobile,region_id,address,bio,postal_code):
        user=self.user
        if user.is_authenticated:
            profile=self.get_by_user(user)
            if profile.id==profile_id or user.has_perm(APP_NAME+'.change_profile'):
                edited_profile=self.objects.get(pk=profile_id)
                
                if edited_profile is not None:
                    edited_profile.first_name=first_name
                    edited_profile.last_name=last_name
                    edited_profile.mobile=mobile
                    edited_profile.region_id=region_id
                    edited_profile.bio=bio
                    edited_profile.address=address
                    edited_profile.postal_code=postal_code
                    
                    edited_profile.save()
                    return edited_profile
        return None
    
    def reset_password(self,request,username,new_password,old_password=None):
        user=self.user
        try:
            selected_user=User.objects.get(username=username)
        except:
            selected_user=None
        
        if selected_user is not None :            
            if self.user is not None and self.user.is_authenticated and self.user.has_perm(APP_NAME+'.change_profile'):                                    
                selected_user.set_password(new_password)
                selected_user.save()
                if selected_user is not None:
                    return True
            selected_user=authenticate(request=request,username=username,password=old_password)                                    
            if selected_user is not None:
                    selected_user.set_password(new_password)
                    selected_user.save()
                    if selected_user is not None:
                        request=self.login(request=request,username=username,password=new_password)
                        return request
                               
    def get(self,profile_id):
        user=self.user
        try:

            profile=self.objects.get(pk=profile_id)
            return profile
        except:
            return None
        
        current_profile=self.get_by_user(user)
        if current_profile is None:
            return None
        if user.has_perm('app.view_profile'):
            profile=self.objects.filter(pk=profile_id)
            if len(profile)==1:
                return profile[0]
        if current_profile.id==profile_id:
            return current_profile
    
    def check_availabe_username(self,username):

        return False if len(User.objects.filter(username=username))>0 else True
    
    def register(self,username,password,first_name,last_name,region_id):
        if not self.check_availabe_username(username):
            return None
        user = User.objects.create_user(username=username,email= 'new_user@khafonline.com', password=password)

        # Update fields and then save again
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        profile=Profile(user=user,first_name=first_name,mobile='',last_name=last_name,region_id=region_id)
        profile.save()
        return profile

    def login(self,request,username,password):
        user=authenticate(request=request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_authenticated:                
                return request  
        return None
    
    def logout(self,request):
        logout(request=request)

    def my_permissions(self):
        user=self.user
        if user.is_superuser:
            return Permission.objects.all()
        return user.user_permissions.all() | Permission.objects.filter(group__user=user)



from .models import *
from dashboard import repo as DashboardRepo
from authentication.repo import ProfileRepo
class MetaDataRepo:
    def __init__(self,user=None):
        self.objects=MetaData.objects
        self.user=user
    def list(self):
        return self.objects.all()
    def list_for_home(self):
        return self.objects.filter(for_home=True)


class LinkRepo:
    def __init__(self,user=None):
        self.user=user
        self.profile=ProfileRepo(user=user).me
        self.objects=Link.objects.order_by('priority')
    def add(self,title,url,priority):
        link=Link(title=title,url=url,priority=priority)
        link.save()
        return link
    def delete(self,link_id,class_session_id):
        link=self.get(link_id=link_id)
        link.delete()
    def search(self,search_for):
        return self.objects.filter(Q(name__contains=search_for) | Q(link__contains=search_for))
    def get(self,link_id):
        try:
            return self.objects.get(pk=link_id)            
        except:
            return None
    def list(self):
        return self.objects.order_by('priority')
    def list_for_home(self):
        return self.objects.filter(for_home=True).order_by('priority')
    def get_nav_items(self):
        return self.objects.filter(for_nav=True).order_by('priority')

class ContactMessageRepo:
    def __init__(self,user=None):
        self.user=user
        self.objects=ContactMessage.objects
    def add(self,full_name,mobile,email,subject,message):
        contact_message=ContactMessage(full_name=full_name,mobile=mobile,email=email,subject=subject,message=message)
        contact_message.save()
        return contact_message
    def list(self):
        if self.user.has_perm(APP_NAME+'.view_contactmessage'):
            return self.objects.all()


class OurTeamRepo(DashboardRepo.OurTeamRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=OurTeam.objects
    

class BlogRepo(DashboardRepo.BlogRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=Blog.objects
    


class FeatureRepo(DashboardRepo.FeatureRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=Feature.objects
    


class ResumeRepo(DashboardRepo.ResumeRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=Resume.objects

class HomeSliderRepo(DashboardRepo.HomeSliderRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=HomeSlider.objects
        
class OurWorkRepo(DashboardRepo.OurWorkRepo):
    def __init__(self,user=None):
        self.user=user
        self.objects=OurWork.objects
    


class ParameterRepo:
    
    def __init__(self,user=None):
        self.objects=Parameter.objects
    
    def set(self,name,value='--'):
        if value is None:
            value='--'
        self.objects.filter(name=name).delete()
        Parameter(name=name,value=value).save()
    
    def init(self,name,value=None):
        if value is None:
            value='...'
        try:
            param=self.objects.get(name=name)
        except :
            self.set(name=name,value=value)

    def get(self,name):
        try:
            parameter=self.objects.get(name=name)
        except:
            self.set(name=name)            
            parameter=self.objects.get(name=name)
        return parameter

        
class MainPicRepo(DashboardRepo.MainPicRepo):    
    def __init__(self,user=None):
        self.objects=MainPic.objects
    
    

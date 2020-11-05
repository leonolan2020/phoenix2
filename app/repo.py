from .models import *
from dashboard import repo as DashboardRepo

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
    

class ParameterRepo(DashboardRepo.ParameterRepo):    
    def __init__(self,user=None):
        self.objects=Parameter.objects
        
class MainPicRepo(DashboardRepo.MainPicRepo):    
    def __init__(self,user=None):
        self.objects=MainPic.objects
    
    

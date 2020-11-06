from django.db import models
from django.shortcuts import reverse
from .apps import APP_NAME
from django.utils.translation import gettext as _
from dashboard import models as DashboardModels


class Link(DashboardModels.Link):
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Link")
        verbose_name = _("Link")
        verbose_name_plural = _("Links")



class MetaData(DashboardModels.MetaData):
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"MetaData")
        verbose_name = _("MetaData")
        verbose_name_plural = _("MetaDatas")



class ContactMessage(DashboardModels.ContactMessage):
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Technology")
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")


   

class Technology(DashboardModels.Technology):

    def save(self):
        self.child_class='technology'
        self.app_name=APP_NAME
        super(Technology,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Technology")
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

class Parameter(DashboardModels.Parameter):
    

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Parameter")
        verbose_name = _("Parameter")
        verbose_name_plural = _("Parameters")
   

class HomeSlider(DashboardModels.HomeSlider):
    

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"HomeSlider")
        verbose_name = _("HomeSlider")
        verbose_name_plural = _("HomeSliders")
   

class OurTeam(DashboardModels.OurTeam):
    

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"OurTeam")
        verbose_name = _("OurTeam")
        verbose_name_plural = _("OurTeams")
   

class OurWork(DashboardModels.OurWork):
    def get_absolute_url(self):
        return reverse(APP_NAME+':ourwork',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(OurWork,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"OurWork")
        verbose_name = _("OurWork")
        verbose_name_plural = _("OurWorks")
   

class Feature(DashboardModels.Feature):
    def get_absolute_url(self):
        return reverse(APP_NAME+':feature',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Feature,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Feature")
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
   

class Resume(DashboardModels.Resume):
    def get_absolute_url(self):
        return reverse(APP_NAME+':resume',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='resume'
        self.app_name=APP_NAME
        super(Resume,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Resume")
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")
   

class Blog(DashboardModels.Blog):
    def get_absolute_url(self):
        return reverse(APP_NAME+':blog',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Blog,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Blog")
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
   


class MainPic(DashboardModels.MainPic):
    def get_absolute_url(self):
        return reverse(APP_NAME+':blog',kwargs={'pk':self.pk})

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"MainPic")
        verbose_name = _("MainPic")
        verbose_name_plural = _("MainPics")
   

# Create your models here.

from django.db import models
from django.shortcuts import reverse
from .apps import APP_NAME
from django.utils.translation import gettext as _
from dashboard import models as DashboardModels


class Technology(DashboardModels.Technology):

    def save(self):
        self.child_class='technology'
        self.app_name=APP_NAME
        super(Technology,self).save()

    
    class Meta:
        verbose_name = _("تکنولوژی")
        verbose_name_plural = _("تکنولوژی ها")
   


class Parameter(DashboardModels.Parameter):
    

    
    class Meta:
        verbose_name = _("پارامتر")
        verbose_name_plural = _("پارامتر ها")
   

class HomeSlider(DashboardModels.HomeSlider):
    

    
    class Meta:
        verbose_name = _("اسلایدر")
        verbose_name_plural = _("اسلایدر ها")
   

class OurTeam(DashboardModels.OurTeam):
    

    
    class Meta:
        verbose_name = _("تیم ما")
        verbose_name_plural = _("اعضای تیم ما")
   

class OurWork(DashboardModels.OurWork):
    def get_absolute_url(self):
        return reverse(APP_NAME+':ourwork',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(OurWork,self).save()

    
    class Meta:
        verbose_name = _("پروژه")
        verbose_name_plural = _("پروژه ها")
   

class Feature(DashboardModels.Feature):
    def get_absolute_url(self):
        return reverse(APP_NAME+':feature',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Feature,self).save()

    
    class Meta:
        verbose_name = _("سرویس")
        verbose_name_plural = _("سرویس ها")
   

class Resume(DashboardModels.Resume):
    def get_absolute_url(self):
        return reverse(APP_NAME+':resume',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Resume,self).save()

    
    class Meta:
        verbose_name = _("رزومه")
        verbose_name_plural = _("رزومه ها")
   

class Blog(DashboardModels.Blog):
    def get_absolute_url(self):
        return reverse(APP_NAME+':blog',kwargs={'pk':self.pk})
    
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Blog,self).save()

    
    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("مقاله ها")
   


class MainPic(DashboardModels.MainPic):
    def get_absolute_url(self):
        return reverse(APP_NAME+':blog',kwargs={'pk':self.pk})

    
    class Meta:
        verbose_name = _("MainPic")
        verbose_name_plural = _("تصویر های اصلی")
   

# Create your models here.

from django.db import models
from django.shortcuts import reverse
from .apps import APP_NAME
from django.utils.translation import gettext as _
from dashboard import models as DashboardModels
from dashboard.settings import ADMIN_URL,MEDIA_URL,STATIC_URL
from .enums import ParametersEnum,MainPicEnum
IMAGE_FOLDER=APP_NAME+'/images/'

class MetaData(DashboardModels.MetaData):
    class Meta:
        default_related_name=_(APP_NAME+"_"+"MetaData")
        verbose_name = _("MetaData")
        verbose_name_plural = _("MetaDatas")

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/metadata/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':metadata',kwargs={'pk':self.pk})
class Link(DashboardModels.Link): 
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Link")
        verbose_name = _("Link")
        verbose_name_plural = _("Links")


    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/link/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':link',kwargs={'pk':self.pk})
class ContactMessage(DashboardModels.ContactMessage):    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"ContactMessage")
        verbose_name = _("ContactMessage")
        verbose_name_plural = _("ContactMessages")

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/contactmessage/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':contactmessage',kwargs={'pk':self.pk})
class Technology(DashboardModels.Technology):

    def save(self):
        self.child_class='technology'
        self.app_name=APP_NAME
        super(Technology,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Technology")
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/technology/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':technology',kwargs={'pk':self.pk})




class HomeSlider(DashboardModels.HomeSlider):
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"HomeSlider")
        verbose_name = _("HomeSlider")
        verbose_name_plural = _("HomeSliders")
   
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/homeslider/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':homeslider',kwargs={'pk':self.pk})

class OurTeam(DashboardModels.OurTeam):

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"OurTeam")
        verbose_name = _("OurTeam")
        verbose_name_plural = _("OurTeams")
   
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/ourteam/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':ourteam',kwargs={'pk':self.pk})

class OurWork(DashboardModels.OurWork):
    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"OurWork")
        verbose_name = _("OurWork")
        verbose_name_plural = _("OurWorks")
   
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/ourwork/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':ourwork',kwargs={'pk':self.pk})

class Feature(DashboardModels.Feature):
    def save(self):
        self.child_class='blog'
        self.app_name=APP_NAME
        super(Feature,self).save()

    
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Feature")
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")
   
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/feature/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':feature',kwargs={'pk':self.pk})

class Resume(DashboardModels.Resume):
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Resume")
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")
   
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/resume/{self.pk}/change/'
    def get_absolute_url(self):
        return reverse(APP_NAME+':resume',kwargs={'pk':self.pk})

class Blog(DashboardModels.Blog):
   
    class Meta:
        default_related_name=_(APP_NAME+"_"+"Blog")
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
   

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/blog/{self.pk}/change/'

    def get_absolute_url(self):
        return reverse(APP_NAME+':blog',kwargs={'pk':self.pk})

class MainPic(models.Model):
    name=models.CharField(_("جای تصویر"), max_length=50,choices=MainPicEnum.choices)    
    image_origin=models.ImageField(_("تصویر"), upload_to=IMAGE_FOLDER+'MainPic/', height_field=None, width_field=None, max_length=None,null=True,blank=True)
    def get_edit_btn(self):
        return f"""
            <a class="" href="{self.get_edit_url()}">
            <i class="material-icons">settings</i>
            ویرایش تصویر
            </a>
        """
    class Meta:
        verbose_name = _("MainPic")
        verbose_name_plural = _("تصویر های اصلی سایت")
    def image(self):
        if self.image_origin is not None and self.image_origin:
            return f'{MEDIA_URL}{str(self.image_origin)}'
        return f'{STATIC_URL}material/img/bg.jpg'
    def __str__(self):
        return self.name

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/mainpic/{self.pk}/change/'

class Parameter(models.Model):

    name=models.CharField(_("نام"), max_length=50,choices=ParametersEnum.choices)
    value=models.CharField(_("مقدار"), max_length=10000)
    
    def get_edit_btn(self):
        return f"""
         <a target="_blank" title="ویرایش {self.name}" class="btn btn-info btn-link" href="{self.get_edit_url()}">
                            <i class="material-icons">settings</i>
                        </a>
        """
    class Meta:
        verbose_name = _("Parameter")
        verbose_name_plural = _("پارامتر ها")

    def __str__(self):
        return f'{self.name} : {self.value}'

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/parameter/{self.pk}/change/'

# Create your models here.

import os
from django.http import Http404,HttpResponse
from django.db import models
from dashboard.settings import ADMIN_URL,MEDIA_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
from tinymce import models as tinymce_models
from django.shortcuts import reverse
IMAGE_FOLDER=APP_NAME+'/images/'
from dashboard.enums import *
from dashboard.constants import *
from .constants import *
from dashboard.models import Page as DashboardPage

class ManagerPage(DashboardPage):
    parent=models.ForeignKey("ManagerPage", verbose_name=_("parent"),null=True,blank=True, on_delete=models.SET_NULL)
 
    def get_breadcrumb_url(self):
        if self.parent is None:
            return f"""<div class="d-inline"><a href="{self.get_absolute_url()}">&nbsp;{self.title}&nbsp;</a></div>"""
        else:
            return self.parent.get_breadcrumb_url()+f"""<span class="text-secondary">&nbsp;/&nbsp;</span><div class="d-inline"><a  href="{self.get_absolute_url()}">&nbsp;{self.title}&nbsp;</a></div>"""
    def childs(self):
      return ManagerPage.objects.filter(parent=self)
    
    def get_link(self):
      icon=self.icon
      if self.icon is None:
        icon="""
        <div class="em15 text-primary" style="font-size:1.5em;">
            <i class="material-icons text-primary" style="font-size:1.5em;">settings</i>
        </div>
        """
      else:
        icon=f"""
         <div class="em15 {self.icon.icon_class}"  style="font-size:1.5em;">
                      {self.icon.get_icon_tag(icon_style='font-size: 1.5em')}
          </div>
        """
      return f"""


         <div class="media mb-2">
                  <div class="icon icon-rose">
                    {icon}
                  </div>
                  <div class="media-body mr-3">
                    <a href="{self.get_absolute_url()}">
                      <h4 class="info-title text-primary text-right">
                        {self.title}

                      </h4>
                    </a>
                    <div class="description text-secondary">
                      {self.short_description if self.short_description else '&nbsp;'}
                   </div>
                  </div>
                </div>

       
        """
    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    
    
    def save(self):
        self.app_name=APP_NAME
        super(ManagerPage,self).save()


class Project(ManagerPage):
    # priority2=models.IntegerField(_("priority"),default=100)
    
    def save(self):
        self.child_class='project'
        super(Project,self).save()



    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    


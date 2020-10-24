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
    
    def get_link(self):
        return f"""
        <a class="" href="{self.get_absolute_url()}">
            {self.icon.get_icon_tag()}  
            {self.title}
        </a>
        """
    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    
    
    def save(self):
        self.app_name=APP_NAME
        super(ManagerPage,self).save()


class Project(ManagerPage):
    priority=models.IntegerField(_("priority"),default=100)
    
    def save(self):
        self.child_class='project'
        super(Project,self).save()



    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    


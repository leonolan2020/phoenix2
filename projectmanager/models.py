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


class Page(models.Model):
    title=models.CharField(_("title"), max_length=50)
    short_description=models.CharField(_("short_description"), max_length=50)    
    description=models.CharField(_("description"), max_length=50)
    icon=models.ForeignKey("dashboard.icon",related_name="projectpages", verbose_name=_("icon"),null=True,blank=True, on_delete=models.SET_NULL)
    color=models.ForeignKey("dashboard.color",related_name="projectpages", verbose_name=_("color"),null=True,blank=True, on_delete=models.SET_NULL)
    color_class=models.CharField(_("color class"),blank=True,null=True,choices=ColorEnum.choices,default=ColorEnum.DEFAULT,max_length=50)
    child_class=models.CharField(_('title'),max_length=200)
    app_name=models.CharField(_('app_name'),null=True,blank=True,max_length=200)
    
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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{self.pk}'




class Project(Page):
    priority=models.IntegerField(_("priority"))
    

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    


from django.core.validators import MinValueValidator,MaxValueValidator
from dashboard.enums import ColorEnum
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
from dashboard.persian import PersianCalendar

class ManagerPage(DashboardPage):
	parent=models.ForeignKey("ManagerPage", verbose_name=_("parent"),null=True,blank=True, on_delete=models.SET_NULL)

	def get_download_url(self):
		return reverse('projectmanager:download_page',kwargs={'pk':self.pk})


	def get_breadcrumb_url(self):
		if self.parent is None:
			return f"""<div class="d-inline"><a href="{self.get_absolute_url()}">&nbsp;{self.title}&nbsp;</a></div>"""
		else:
			return self.parent.get_breadcrumb_url()+f"""<span class="text-secondary">&nbsp;/&nbsp;</span><div class="d-inline"><a  href="{self.get_absolute_url()}">&nbsp;{self.title}&nbsp;</a></div>"""
	def childs(self):
		return ManagerPage.objects.filter(parent=self)



	def persian_date_added(self):
		return PersianCalendar().from_gregorian(self.date_added)

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
                      <h4 class="info-title text-{self.color} text-right">
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
	percent=models.IntegerField(_('درصد پیشرفت'),default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
	start_date=models.DateField(_("شروع"),null=True,blank=True, auto_now=False, auto_now_add=False)
	end_date=models.DateField(_("پایان"),null=True,blank=True, auto_now=False, auto_now_add=False)
	def persian_start_date(self):
		return PersianCalendar().from_gregorian_date(self.start_date)
	def persian_end_date(self):
		return PersianCalendar().from_gregorian_date(self.end_date)

	def get_resource(self):
		return self.color
		if self.color==ColorEnum.SUCCESS:
			return 'spring'
		
		if self.color==ColorEnum.DANGER:
			return 'sports'
		
		if self.color==ColorEnum.WARNING:
			return 'winter'
		
		if self.color==ColorEnum.INFO:
			return 'autumn'
		
		if self.color==ColorEnum.ROSE:
			return 'summer'
		
		if self.color==ColorEnum.PRIMARY:
			return 'summer'
		
		if self.color==ColorEnum.DEFAULT:
			return 'sports'
		
		
		if self.color==ColorEnum.SECONDARY:
			return 'autumn'
		

	events=models.ManyToManyField("Event",blank=True, verbose_name=_("رویداد ها"))
	contractors=models.ManyToManyField("Contractor",blank=True, verbose_name=_("پیمانکار ها"))
	organiazation_units=models.ManyToManyField("OrganiazationUnit",blank=True, verbose_name=_("واحد های سازمانی"))
	location=models.TextField(_('موقعیت در نقشه گوگل مپ'),null=True,blank=True)
	def save(self):
		self.child_class='project'
		super(Project,self).save()

	def get_guantt_url(self):
		return reverse('projectmanager:guantt',kwargs={'pk':self.pk})
	def childs(self):
		return Project.objects.filter(parent=self).order_by('start_date')
	class Meta:
		verbose_name = _("Project")
		verbose_name_plural = _("Projects")


class OrganiazationUnit(ManagerPage):

	def parent_title(self):
		if self.parent is not None:
			return self.parent.title

	def caption(self):
		return f"""
		<strong>
		{self.title}
		</strong>
		<small>
		<small>
		{self.short_description}
		</small>		
		</small>
		
		"""

	class Meta:
		verbose_name = _("OrganiazationUnit")
		verbose_name_plural = _("OrganiazationUnits")

	def save(self):
		self.child_class='organiazationunit'
		super(OrganiazationUnit,self).save()


class Event(ManagerPage):
	event_date=models.DateTimeField(_("event_date"), auto_now=False, auto_now_add=False)

	def persian_event_date(self):
		return PersianCalendar().from_gregorian(self.event_date)

	def get_tag(self):
		event=self
		return f"""
		 <div class="timeline-badge {event.color}">
                    {event.icon.get_icon_tag(color=ColorEnum.LIGHT)}
                </div>
                <div class="timeline-panel">
                    <div class="timeline-heading">
                        <span class="badge badge-pill badge-danger">
                            {event.title}
                        </span>
                        <span title="{event.event_date.strftime("%Y/%m/%d %H:%M:%S")}" class="text-secondary" style="float: right;">
                            <small>
                                {event.persian_event_date()}
                            </small> </span>
                    </div>
                    <div class="timeline-body">
                    <p>   {event.short_description}<p>
                    </div>
                    <a class="btn btn-light btn-sm btn-round" href="{event.get_absolute_url()}">
                        <i class="material-icons">description</i>
                        <small>
                            <small>
                                جزییات بیشتر
                            </small>
                        </small>
                    </a>
                </div>
		"""
	class Meta:
		verbose_name = _("Event")
		verbose_name_plural = _("Events")

	def save(self):
		self.child_class='event'
		super(Event,self).save()


class Contractor(ManagerPage):

	

	class Meta:
		verbose_name = _("Contractor")
		verbose_name_plural = _("Contractors")

	def save(self):
		self.child_class='contractor'
		super(Contractor,self).save()



class ArchiveDocument(ManagerPage):
	

	class Meta:
		verbose_name = _("ArchiveDocument")
		verbose_name_plural = _("اسناد آرشیوی")

	def save(self):
		self.child_class='archivedocument'
		super(ArchiveDocument,self).save()






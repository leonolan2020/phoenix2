from django.contrib.auth.models import Group
from utility.persian import PersianCalendar
from dashboard.models import Page as DashboardPage
from .constants import *
from dashboard.constants import *
from dashboard.enums import *
from django.core.validators import MinValueValidator, MaxValueValidator
from dashboard.enums import ColorEnum
from .enums import StatusColor,MaterialRequestStatusEnum,SignatureStatusEnum
import os
from django.http import Http404, HttpResponse
from django.db import models
from dashboard.settings import ADMIN_URL, MEDIA_URL
from .apps import APP_NAME
from django.utils.translation import gettext as _
from .enums import *
from tinymce import models as tinymce_models
from django.shortcuts import reverse
IMAGE_FOLDER = APP_NAME+'/images/'


class ManagerPage(DashboardPage):
    parent = models.ForeignKey("ManagerPage", verbose_name=_(
        "parent"), null=True, blank=True, on_delete=models.SET_NULL)

    def get_download_url(self):
        return reverse('projectmanager:download_page', kwargs={'pk': self.pk})
    def get_presentation_url(self):
        return reverse('projectmanager:presentation', kwargs={'pk': self.pk})

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
        icon = self.icon
        if self.icon is None:
            icon = """
        <div class="em15 text-primary" style="font-size:1.5em;">
            <i class="material-icons text-primary" style="font-size:1.5em;">settings</i>
        </div>
        """
        else:
            icon = f"""
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
                        <p>
                         {self.short_description if self.short_description else '&nbsp;'}
                        </p>
                   </div>
                  </div>
                </div>


        """

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")

    def save(self):
        self.app_name = APP_NAME
        super(ManagerPage, self).save()

    def get_absolute_url(self):
        return reverse(APP_NAME+':'+self.child_class, kwargs={'pk': self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/{self.child_class}/{self.pk}/change/'


class Project(ManagerPage):
    # priority2=models.IntegerField(_("priority"),default=100)
    percent = models.IntegerField(_('درصد پیشرفت'), default=0, validators=[
                                  MinValueValidator(0), MaxValueValidator(100)])
    start_date = models.DateField(
        _("شروع"), null=True, blank=True, auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("پایان"), null=True,
                                blank=True, auto_now=False, auto_now_add=False)
    # organization_units=models.ManyToManyField("OrganizationUnit",verbose_name=_('organization_units'),blank=True)
    events = models.ManyToManyField(
        "Event", blank=True, verbose_name=_("رویداد ها"))
    contractors = models.ManyToManyField(
        "Contractor", blank=True, verbose_name=_("پیمانکار ها"))
    organization_units = models.ManyToManyField(
        "OrganizationUnit", blank=True, verbose_name=_("واحد های سازمانی"))
    location = models.TextField(
        _('موقعیت در نقشه گوگل مپ'), null=True, blank=True)
    def persian_start_date(self):
        return PersianCalendar().from_gregorian_date(self.start_date)

    def persian_end_date(self):
        return PersianCalendar().from_gregorian_date(self.end_date)

    def get_resource(self):
        return self.color
        if self.color == ColorEnum.SUCCESS:
            return 'spring'

        if self.color == ColorEnum.DANGER:
            return 'sports'

        if self.color == ColorEnum.WARNING:
            return 'winter'

        if self.color == ColorEnum.INFO:
            return 'autumn'

        if self.color == ColorEnum.ROSE:
            return 'summer'

        if self.color == ColorEnum.PRIMARY:
            return 'summer'

        if self.color == ColorEnum.SECONDARY:
            return 'autumn'

    

    def save(self):
        self.child_class = 'project'
        super(Project, self).save()

    def get_guantt_url(self):
        return reverse('projectmanager:guantt', kwargs={'pk': self.pk})

    def childs(self):
        return Project.objects.filter(parent=self).order_by('start_date')

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")
    def material_requests(self):
        return MaterialRequest.objects.filter(project=self)

class Employee(models.Model):
    profile = models.ForeignKey("authentication.Profile", related_name='employee_set_m', verbose_name=_(
        "profile"), null=True, blank=True, on_delete=models.PROTECT)
    work_unit = models.ForeignKey("OrganizationUnit", verbose_name=_(
        "work_unit"), null=True, blank=True, on_delete=models.PROTECT)

    role = models.CharField(_("نقش"), choices=EmployeeEnum.choices,
                            default=EmployeeEnum.DEFAULT, max_length=50)
    degree = models.CharField(_("مدرک"), choices=DegreeLevelEnum.choices,
                              default=DegreeLevelEnum.KARSHENASI, max_length=50)
    major = models.CharField(
        _("رشته تحصیلی"), null=True, blank=True, max_length=50)
    introducer = models.CharField(
        _("معرف"), null=True, blank=True, max_length=50)

    def __str__(self):
        return self.profile.name()+' '+self.role+((' '+self.work_unit.title) if self.work_unit else '')

    def get_link(self):
        return f"""<a href="{self.get_absolute_url()}">
                <i class="fa fa-user"></i>
                {self.profile.name()}
            </a>"""

    def my_assignments(self):
        return Assignment.objects.filter(assign_to=self)

    def save(self):
        if self.profile.user:
            # self.profile.user.groups.delete()
            pass
        if self.work_unit and self.profile.user:
            group_name = self.role+' '+self.work_unit.title
            try:
                origin_group = Group.objects.get(name=group_name)
            except:
                Group.objects.filter(name=group_name).delete()
                origin_group = None
            if origin_group is None:
                origin_group = Group(name=group_name)
                origin_group.save()
            if origin_group is not None:
                if self.profile.user is not None:
                    self.profile.user.groups.add(origin_group)
        super(Employee, self).save()

    def name(self):
        if self.profile is not None:
            return f'{self.profile.name()} {self.role}'
        return f'{self.role}'

    class Meta:
        verbose_name = _("Employee")
        verbose_name_plural = _("Employees - کارکنان")

    def get_absolute_url(self):
        return reverse(APP_NAME+':employee',kwargs={'pk':self.pk})

    def get_edit_url(self):
        if self.profile is not None:
            return self.profile.get_edit_url()


class Assignment(ManagerPage):
    
    project_for = models.ForeignKey("Project",related_name='project_assignments',null=True,blank=True, verbose_name="پروژه مربوط", on_delete=models.PROTECT)
    assign_to = models.ForeignKey("Employee", verbose_name="کاربر مربوط", on_delete=models.PROTECT)
    status = models.CharField(_('status'), max_length=50,choices=AssignmentStatusEnum.choices, default=AssignmentStatusEnum.DEFAULT)

    def save(self):
        self.child_class = 'assignment'
        self.app_name = APP_NAME
        super(Assignment, self).save()

    class Meta:
        verbose_name = _("Assignment")
        verbose_name_plural = _("Assignments - تکلیف ها")

    def __str__(self):
        return f'{self.title} - {self.assign_to.profile.name()}'

    def get_status_color(self):
        return StatusColor(self.status)


class OrganizationUnit(ManagerPage):

	def parent_title(self):
		if self.parent is not None:
			return self.parent.title

	def childs(self):
		return OrganizationUnit.objects.filter(parent=self)

	def get_template(self):
		template = f"""
		<div>
		<h4 class="mt-4">
			<a class="text-{self.color} mb-2" href="{self.get_absolute_url()}">
				{self.icon.get_icon_tag() if self.icon else '<i class="material-icons">apartment</i>'}
				{self.title}</a>  
			</h4>
		"""
		for employee in self.employee_set.all():
			template += f"""
		        <div class="">
		            <small>
		                <a class="d-inline mr-5 text-secondary" href="{employee.profile.get_absolute_url()}">
		                <i class="fa fa-user"></i>
		                {employee.profile.name()}</a>

		                <span class="badge badge-info">{employee.role}</span>
		            </small>
		        </div>
		    	"""
		template += """
		<hr>
		<div class="mr-5">
		"""
		for work_unit1 in self.childs():
			template += work_unit1.get_template()
		template += """
		</div>
		"""

		template += '</div>'
		return template

	def employees_caption(self):
		caption=""
		for employee in self.employee_set.all():
			caption += f"""{employee.profile.name()} ( {employee.role} )
			"""
		return caption

	def caption(self):
		show_employees=False
		icon=self.icon.get_icon_tag(color=ColorEnum.PRIMARY) if self.icon is not None else ''
		icon=''
		caption = f"""
		<strong>
		<a href="{self.get_absolute_url()}">
		
			{icon}
		{self.title}
		</a>
		</strong>
	    """
		if show_employees:
			for employee in self.employee_set.all():
				caption += f"""

                <div>
                <small>

                <small style="direction:rtl;">
                <i class="fa fa-user"></i>
                <a href="{employee.get_absolute_url()}">
                
                    {employee.profile.name()}
                    </a>
                </small>
                </small>		
                </div>
                """
		caption += """ """
		return caption

	class Meta:
		verbose_name = _("OrganizationUnit")
		verbose_name_plural = _("OrganizationUnits")

	def save(self):
		if self.child_class is None:
			self.child_class = 'organizationunit'
		super(OrganizationUnit, self).save()

	def employees(self):
		return self.employee_set.all()


class Event(ManagerPage):
    event_date = models.DateTimeField(
        _("event_date"), auto_now=False, auto_now_add=False)

    def persian_event_date(self):
        return PersianCalendar().from_gregorian(self.event_date)

    def get_tag(self):
        event = self
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
        self.child_class = 'event'
        super(Event, self).save()


class Contractor(ManagerPage):

    class Meta:
        verbose_name = _("Contractor")
        verbose_name_plural = _("Contractors")

    def save(self):
        self.child_class = 'contractor'
        super(Contractor, self).save()


class ArchiveDocument(ManagerPage):

    class Meta:
        verbose_name = _("ArchiveDocument")
        verbose_name_plural = _("اسناد آرشیوی")

    def save(self):
        self.child_class = 'archivedocument'
        super(ArchiveDocument, self).save()



class MaterialBrand(ManagerPage):
    
    def save(self):
        self.child_class='materialbrand'
        super(MaterialBrand,self).save()
    rate=models.IntegerField(_("امتیاز"),default=0)    
    url=models.CharField(_("آدرس اینترتی"),null=True,blank=True,max_length=100)


    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands - برند های متریال")

 

    def get_edit_url(self):
        return ADMIN_URL+APP_NAME+'/brand/'+str(self.pk)+'/change/'


class MaterialCategory(ManagerPage):
    
    def save(self):
        self.child_class='materialcategory'
        super(MaterialCategory,self).save()
    
    rate=models.IntegerField(_("امتیاز"),default=0)
    def materials(self):
        return Material.objects.filter(category=self)
    
   
    class Meta:
        verbose_name = _("MaterialCategory")
        verbose_name_plural = _("MaterialCategories - دسته بندی های متریال")


class Material(ManagerPage):
    
    def save(self):
        self.child_class='material'
        super(Material,self).save()
    brand=models.ForeignKey("MaterialBrand",null=True,blank=True,verbose_name=_("brand"), on_delete=models.CASCADE)
    model=models.CharField(_("model"),null=True,blank=True, max_length=50)
    # category=models.ForeignKey("MaterialCategory",related_name='material_category',on_delete=models.PROTECT)
    unit_name=models.CharField(_('واحد'),null=True,blank=True,max_length=50)
    
     

    class Meta:
        verbose_name = _("Material")
        verbose_name_plural = _("Materials -  متریال ها")


class MaterialWareHouse(OrganizationUnit):
    
    def save(self):
        # if self.location:
        #     self.location=self.location.replace('width="600"','width="100%"')
        #     self.location=self.location.replace('height="450"','height="400"')
        
        self.child_class='materialwarehouse'
        super(MaterialWareHouse,self).save()
    address=models.CharField(_("آدرس"),null=True,blank=True, max_length=50)
    class Meta:
        verbose_name = _("MaterialWareHouse")
        verbose_name_plural = _("MaterialWareHouses - انبار های متریال")
    def employees(self):
        return []
    def materials(self):
        materialinstock_set=self.materialinstock_set.all()
        # MaterialObject.objects.filter(id__in=self.materialinstock_set.values('material_object_id'))
        # materials=materialobject_set.all()
        return materialinstock_set.order_by('material_object')
    def materials3(self):
        materialinstock_set=self.materialinstock_set.all()
        # materialobject_set=MaterialObject.objects.filter(id__in=list(materialinstock_set.values('material_object_id')))
        # material_set=materialobject_set.only('material')
        # MaterialObject.objects.filter(id__in=self.materialinstock_set.values('material_object_id'))
        # materials=materialobject_set.all()
        materialobjects = MaterialObject.objects.filter(
            id__in=materialinstock_set.values('material_object_id')
        )

        materials=Material.objects.all().annotate(
        most_benevolent_hero=Subquery(
                materialobjects.values('material')[:1]
            )
        )

        materials=materialobjects.annotate(
        most_benevolent_hero=Count('material')
        )

        return materials
    def materials2(self):
        materialinstock_set=self.materialinstock_set.all()
        # materialobject_set=MaterialObject.objects.filter(id__in=list(materialinstock_set.values('material_object_id')))
        # material_set=materialobject_set.only('material')
        # MaterialObject.objects.filter(id__in=self.materialinstock_set.values('material_object_id'))
        # materials=materialobject_set.all()
        materialobjects = MaterialObject.objects.filter(
            id__in=materialinstock_set.values('material_object_id')
        )
        materials=materialobjects.raw('SELECT COUNT(*) AS count1,id,material_id FROM projectmanager_materialobject GROUP BY material_id')
        materials1=Material.objects.all().annotate(
        most_benevolent_hero=Subquery(
                materialobjects.values('material')[:1]
            )
        )

        materials1=materialobjects.annotate(
        most_benevolent_hero=Count('material')
        )

        return materials


class MaterialObject(models.Model):
    material=models.ForeignKey("Material", verbose_name=_("material"), on_delete=models.CASCADE)
    serial_no=models.CharField(_('serial_no'),null=True,blank=True,max_length=200)
    barcode1=models.CharField(_('barcode1'),null=True,blank=True,max_length=200)
    borcode2=models.CharField(_('barcode2'),null=True,blank=True,max_length=200)
    barcode3=models.CharField(_('barcode3'),null=True,blank=True,max_length=200)
    package_no=models.CharField(_("package_no"), null=True,blank=True,max_length=50)
    package_name=models.CharField(_("package_name"), null=True,blank=True,max_length=50)
    

    class Meta:
        verbose_name = _("MaterialObject")
        verbose_name_plural = _("MaterialObjects- متریال های موجود")

    def __str__(self):
        return f'{self.material.title} {self.serial_no if self.serial_no else "با شناسه"+str(self.pk)}'

    def get_absolute_url(self):
        return reverse('projectmanager:materialobject',kwargs={'materialobject_id':self.pk})

    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/materialobject/{self.pk}/change/'


class MaterialPackage(models.Model):
    
    pack_no=models.CharField(_("pack_no"), max_length=50)
    material_objects=models.ManyToManyField("MaterialObject", verbose_name=_("material_objects"))
     

    class Meta:
        verbose_name = _("MaterialPackage")
        verbose_name_plural = _("MaterialPackages - پکیج های متریال")

    def __str__(self):
        return f'{self.pack_no} {self.name}'

    def get_absolute_url(self):
        return reverse("MaterialPackage_detail", kwargs={"pk": self.pk})


class MaterialInStock(models.Model):
    material_object=models.ForeignKey("MaterialObject", verbose_name=_("متریال"), on_delete=models.CASCADE)
    warehouse=models.ForeignKey("MaterialWareHouse", verbose_name=_("انبار متریال"), on_delete=models.CASCADE)
    row=models.IntegerField(_('قفسه'))
    col=models.IntegerField(_('ردیف'))
    date_added=models.DateTimeField(_('تاریخ ثبت') , auto_now_add=True,auto_now=False)
    date_opi=models.DateTimeField(_('تاریخ opi') , auto_now_add=False,auto_now=False,null=True,blank=True)

    class Meta:
        verbose_name = _("MaterialInStock")
        verbose_name_plural = _("MaterialInStocks- متریال های موجود در انبار")

    def __str__(self):
        return str(self.material_object)+str(self.warehouse)
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/materialinstock/{self.pk}/change'    


class MaterialRequest(models.Model):
    material=models.ForeignKey("Material", verbose_name=_("متریال"), on_delete=models.PROTECT)
    quantity=models.IntegerField(_("تعداد"))
    project=models.ForeignKey("Project", verbose_name=_("پروژه"), on_delete=models.PROTECT)
    description=models.CharField(_("توضیحات"),null=True,blank=True,default='', max_length=50)
    profile=models.ForeignKey("authentication.Profile", verbose_name=_("تحویل گیرنده"), on_delete=models.PROTECT)
    date_added=models.DateTimeField(_("تاریخ درخواست"), auto_now=False, auto_now_add=True)
    date_delivered=models.DateTimeField(_("تاریخ درخواست"),null=True,blank=True, auto_now=False, auto_now_add=False)
    status=models.CharField(_("وضعیت"),choices=MaterialRequestStatusEnum.choices,default=MaterialRequestStatusEnum.DEFAULT, max_length=50)

    class_name='materialrequest'

    class Meta:
        verbose_name = _("MaterialRequest")
        verbose_name_plural = _("درخواست های متریال")
    def persian_date_delivered(self):
        return PersianCalendar().from_gregorian(self.date_delivered)
    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)
    def __str__(self):
        return f'{self.project.title} ___  {self.material.title} #{self.quantity} {self.material.unit_name}'

    def get_absolute_url(self):
        return reverse(f'{APP_NAME}:{self.class_name}', kwargs={"pk": self.pk})
    def get_edit_url(self):
        return f'{ADMIN_URL}{APP_NAME}/{self.class_name}/{self.pk}/change/'
    def get_status_color(self):
        return StatusColor(self.status)

    def get_status_tag(self):
        return f"""<span class="badge badge-pill badge-{self.get_status_color()}">{self.status}</span>"""
    def signatures(self):
        return MaterialRequestSignature.objects.filter(materialrequest=self).order_by('-date_added')


class MaterialRequestSignature(models.Model):
    materialrequest=models.ForeignKey("materialrequest", verbose_name=_("درخواست"), on_delete=models.PROTECT)
    profile=models.ForeignKey("authentication.Profile", verbose_name=_("profile"), on_delete=models.PROTECT)
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    description=models.CharField(_("description"), max_length=200)
    status=models.CharField(_("status"),choices=SignatureStatusEnum.choices,default=SignatureStatusEnum.DEFAULT, max_length=200)
    class Meta:
        verbose_name = _("MaterialRequestSignature")
        verbose_name_plural = _("امضا ها")

    def __str__(self):
        return f'{self.profile.name()} : {self.description} @ {PersianCalendar().from_gregorian(self.date_added)}'

    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)
    
    def get_status_color(self):
        return StatusColor(self.status)
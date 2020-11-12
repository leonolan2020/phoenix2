import random
from .models import MaterialRequestSignature,MaterialRequest,Material,MaterialInStock,MaterialWareHouse, Assignment, Project, Event, OrganizationUnit, Employee, Contractor, ManagerPage, ArchiveDocument
from authentication.repo import ProfileRepo
from dashboard.models import Icon
from dashboard.enums import ColorEnum, IconsEnum
from django.db.models import Q, F
from authentication.models import Profile
import datetime


class MaterialRequestRepo:
	def __init__(self, user=None):
		self.objects = MaterialRequest.objects
		self.user = user
	def list(self):
		return self.objects.all()
	def materialrequest(self, materialrequest_id):
		try:
			return self.objects.get(pk=materialrequest_id)
		except:
			return None
	
	def do_signature(self,status,description,materialrequest_id):
		profile=ProfileRepo(user=self.user).me
		if profile is not None :
			materialrequest=self.materialrequest(materialrequest_id=materialrequest_id)
			if materialrequest is not None:
				signature=MaterialRequestSignature(profile=profile,status=status,description=description,materialrequest=materialrequest)
				signature.save()
				materialrequest.status=status
				materialrequest.save()
				return signature

class MaterialWareHouseRepo:
	def __init__(self, user=None):
		self.objects = MaterialWareHouse.objects
		self.user = user
	def list(self):
		return self.objects.all()
	def materialwarehouse(self, materialwarehouse_id):
		try:
			return self.objects.get(pk=materialwarehouse_id)
		except:
			return None
	def list_materials_in_stock(self,materialwarehouse_id):
		materialwarehouse=self.materialwarehouse(materialwarehouse_id=materialwarehouse_id)
		if materialwarehouse is not None:
			return MaterialInStock.objects.filter(warehouse=materialwarehouse)
	def add(self,parent_id,title):
		parent=self.materialwarehouse(materialwarehouse_id=parent_id)
		icon = Icon(icon_material='engineering',icon_title='آیکون '+title, color=ColorEnum.PRIMARY)
		icon.save()
		materialwarehouse=MaterialWareHouse(title=title,parent=parent,icon=icon,short_description='',description='')
		materialwarehouse.save()
		return materialwarehouse


class MaterialRepo:
    def __init__(self, user=None):
        self.objects = Material.objects
        self.user = user

    def material(self, material_id):
        try:
            return self.objects.get(pk=material_id)
        except:
            return None
  

class AssignmentRepo:
    def __init__(self, user):
        self.objects = Assignment.objects
        self.user = user
        self.profile = ProfileRepo(user=user).me

    def assignment(self, assignment_id):
        try:
            return self.objects.get(pk=assignment_id)
        except:
            return None

    def my_assignments(self):
        me = EmployeeRepo(user=self.user).me
        assignments = self.objects.filter(assign_to=me)
        return assignments

class EmployeeRepo:
    def __init__(self, user):
        self.objects = Employee.objects
        self.user = user
        self.profile = ProfileRepo(user=user).me
        try:
            self.me = self.objects.get(profile=self.profile)
        except:
            self.me = None

    def add(self, role, org_unit_id, first_name, last_name):
        profile = Profile(first_name=first_name, last_name=last_name)
        profile.save()
        work_unit = OrganizationUnitRepo(user=self.user).organizationunit(
            organizationunit_id=org_unit_id)
        if work_unit is not None:
            employee = Employee(
                profile=profile, work_unit=work_unit, role=role)
            employee.save()
            return employee

    def employee(self, employee_id):
        try:
            return self.objects.get(pk=employee_id)
        except:
            return None


class ManagerPageRepo:
    def __init__(self, user=None):
        self.objects = ManagerPage.objects
        self.user = user

    def list(self):
        return self.objects.all()

    def search(self, search_for):
        return self.objects.filter(Q(title__contains=search_for) | Q(short_description__contains=search_for))

    def page(self, page_id):
        try:
            return self.objects.get(pk=page_id)
        except:
            return None


class ContractorRepo:
    def __init__(self, user=None):
        self.objects = Contractor.objects
        self.user = user
        self.profile = ProfileRepo(user=user).me
        try:
            self.me = self.objects.get(profile=self.profile)
        except:
            self.me = None

    def list(self):
        return self.objects.all()

    def add(self, title):
        icon = Icon(icon_material='engineering',
                    icon_title='آیکون '+title, color=ColorEnum.PRIMARY)
        icon.save()
        contractor = Contractor(icon=icon, title=title,
                                short_description='', description='')
        contractor.save()
        if contractor is not None:
            return contractor

    def contractor(self, contractor_id):
        try:
            return self.objects.get(pk=contractor_id)
        except:
            return None


class EventRepo:
    def __init__(self, user=None):
        self.objects = Event.objects
        self.user = user
        self.profile = ProfileRepo(user=user).me

    def list_for_project(self, project_id):
        project = ProjectRepo(user=self.user).project(project_id=project_id)
        if project is not None:
            return self.objects.filter(project=project)

    def event(self, event_id):
        try:
            return self.objects.get(pk=event_id)
        except:
            return None

    def add(self, title, short_description, project_id, event_date, color=None):
        if color is None:
            color = ColorEnum.DANGER
        project = ProjectRepo(user=self.user).project(project_id=project_id)
        if project is not None and self.profile is not None:
            icon = Icon(icon_title='event icon', color=color,
                        icon_fa='fa fa-calendar')
            icon.save()
            event = Event(profile=self.profile, color=color, icon=icon, title=title,
                          short_description=short_description, event_date=event_date)
            event.save()
            project.events.add(event)
            project.save()
            return event


class ArchiveDocumentRepo:
    def __init__(self, user=None):
        self.objects = ArchiveDocument.objects
        self.user = user
        self.profile = ProfileRepo(user=user).me

    def list_roots(self):
        return self.objects.filter(parent=None)

    def archivedocument(self, archivedocument_id):
        try:
            return self.objects.get(pk=archivedocument_id)
        except:
            return None

    def add(self, title, parent_id):
        if parent_id == 0:
            parent = None
        else:
            parent = self.archivedocument(archivedocument_id=parent_id)
        icon = Icon(color=ColorEnum.PRIMARY,
                    icon_material='dashboard', icon_title='آیکون '+title)
        icon.save()

        archivedocument = ArchiveDocument(
            parent=parent, icon=icon, title=title, short_description='', description='')
        archivedocument.save()
        if archivedocument is not None:
            return archivedocument


class OrganizationUnitRepo():
    def __init__(self, user=None):
        self.objects = OrganizationUnit.objects
        self.user = user

    def list_roots(self):
        return self.objects.filter(parent=None).order_by('-priority')

    def list(self):
        return self.objects.order_by('-priority')

    def organizationunit(self, organizationunit_id):
        try:
            return self.objects.get(pk=organizationunit_id)
        except:
            return None

    def add(self, title, parent_id):
        if parent_id == 0:
            parent = None
        else:
            parent = self.organizationunit(organizationunit_id=parent_id)
        icon = Icon(color=ColorEnum.PRIMARY,
                    icon_material='apartment', icon_title='آیکون '+title)
        icon.save()

        organizationunit = OrganizationUnit(
            parent=parent, icon=icon, title=title, short_description='', description='')
        organizationunit.save()
        if organizationunit is not None:
            return organizationunit


class ProjectRepo:
    def __init__(self, user=None):
        self.objects = Project.objects
        self.user = user
        self.profile = ProfileRepo(user=self.user).me
        self.me_employee = EmployeeRepo(user=self.user).me
        self.me_contractor = ContractorRepo(user=self.user).me
        # must be deleted
        # print('me_employee')
        # print(self.me_employee)
        # print('me_contractor')
        # print(self.me_contractor)

    def my_projects(self):
        if self.me_contractor is not None:
            return self.me_contractor.project_set.all()
        if self.me_employee is not None:
            return self.me_employee.work_unit.project_set.all()

    def list_roots(self):
        return self.objects.filter(parent=None).order_by('-priority')

    def list(self):
        return self.objects.order_by('-priority')

    def get_roots(self):
        return self.objects.filter(parent=None)

    def project(self, project_id):
        try:
            return self.objects.get(pk=project_id)
        except:
            return None

    def edit_timing(self, project_id, start_date, end_date, percent):
        project = self.project(project_id=project_id)
        if project is not None:
            project.start_date = start_date
            project.end_date = end_date
            project.percent = percent
            project.save()
            return project

    def get(self, pk):
        try:
            return self.objects.get(pk=pk)
        except:
            return None

    def go_up(self, pk):
        down_object = self.get(pk=pk)
        try:
            up_object = self.objects.get(priority=down_object.priority)
        except:
            up_object = None
        if down_object is not None:
            down_object.priority = down_object.priority+1
            down_object.save()
        if up_object is not None:
            up_object.priority = up_object.priority-1
            up_object.save()

    def go_down(self, pk):
        up_object = self.get(pk=pk)
        try:
            down_object = self.objects.get(priority=down_object.priority)
        except:
            down_object = None
        if down_object is not None:
            down_object.priority = down_object.priority-1
            down_object.save()
        if up_object is not None:
            up_object.priority = up_object.priority+1
            up_object.save()

    def add(self, title, parent_id):
        if parent_id == 0:
            parent = None
        else:
            parent = self.project(project_id=parent_id)
        color = random.choices(ColorEnum.choices)[0][0]
        if color == ColorEnum.LIGHT:
            color = ColorEnum.PRIMARY
        icon = Icon(color=color, icon_material=random.choices(
            IconsEnum.choices)[0][0], icon_title='آیکون '+title)
        icon.save()
        start_date = datetime.datetime.now().date()
        end_date = (start_date + datetime.timedelta(days=2))
        percent = random.choices(range(5))[0]

        project = Project(percent=percent, color=color, start_date=start_date, end_date=end_date,
                          parent=parent, icon=icon, title=title, short_description='', description='')
        project.save()
        if project is not None:
            return project

    def edit_location(self, project_id, location):
        project = self.project(project_id=project_id)
        if project is not None:
            location = location.replace('width="600"', 'width="100%"')
            location = location.replace('height="450"', 'height="400"')
            project.location = location
            project.save()
            return project

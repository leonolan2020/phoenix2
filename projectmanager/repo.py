from .models import Project,Event,OrganiazationUnit,Contractor
from authentication.repo import ProfileRepo
from dashboard.models import Icon
from dashboard.enums import ColorEnum

class ContractorRepo:
    def __init__(self,user=None):
        self.objects=Contractor.objects
        self.user=user
    def list(self):
        return self.objects.all()
    def add(self,title):
        icon=Icon(icon_material='engineering',icon_title='آیکون '+title,color=ColorEnum.PRIMARY)
        icon.save()
        contractor=Contractor(icon=icon,title=title,short_description='',description='')
        contractor.save()
        if contractor is not None:
            return contractor
             
    def contactor(self,contactor_id):
        try:
            return self.objects.get(pk=contactor_id)
        except:
            return None

class EventRepo:
    def __init__(self,user=None):
        self.objects=Event.objects
        self.user=user
    def list_for_project(self,project_id):
        project=ProjectRepo(user=self.user).project(project_id=project_id)
        if project is not None:
            return self.objects.filter(project=project)
    def event(self,event_id):
        try:
            return self.objects.get(pk=event_id)
        except:
            return None

class OrganiazationUnitRepo():
    def __init__(self,user=None):
        self.objects=OrganiazationUnit.objects
        self.user=user
    def list_roots(self):
        return self.objects.filter(parent=None).order_by('-priority')
    def organiazationunit(self,organiazationunit_id):
        try:
            return self.objects.get(pk=organiazationunit_id)
        except:
            return None 
class ProjectRepo:
    def __init__(self,user=None):
        self.objects=Project.objects
        self.user=user
        self.profile=ProfileRepo(user=self.user).me
        # self.me_employee=EmployeeRepo(user=self.user).me
        # self.me_contractor=ContractorRepo(user=self.user).me
        #must be deleted
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
    def project(self,project_id):
        try:
            return self.objects.get(pk=project_id)
        except:
            return None
    def get(self,pk):
        try:
            return self.objects.get(pk=pk)
        except:
            return None
    def go_up(self,pk):
        down_object=self.get(pk=pk)
        try:
            up_object=self.objects.get(priority=down_object.priority)
        except:
            up_object=None
        if down_object is not None:
            down_object.priority=down_object.priority+1
            down_object.save()
        if up_object is not None:
            up_object.priority=up_object.priority-1
            up_object.save()

    def go_down(self,pk):
        up_object=self.get(pk=pk)
        try:
            down_object=self.objects.get(priority=down_object.priority)
        except:
            down_object=None
        if down_object is not None:
            down_object.priority=down_object.priority-1
            down_object.save()
        if up_object is not None:
            up_object.priority=up_object.priority+1
            up_object.save()

    def add(self,title,parent_id):
        if parent_id==0:
            parent=None
        else:
            parent=self.project(project_id=parent_id)
        icon=Icon(icon_material='dashboard',icon_title='آیکون '+title)
        icon.save()
        project=Project(parent=parent,icon=icon,title=title,short_description='',description='')
        project.save()
        if project is not None:
            return project
             
              
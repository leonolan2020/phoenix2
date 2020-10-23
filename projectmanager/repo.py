from .models import Project
from authentication.repo import ProfileRepo



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
        parent=self.project(project_id=parent_id)
        project=Project(color='primary',parent=parent,icon='construction',title=title)
        project.save()
        if project is not None:
            return project
             
              
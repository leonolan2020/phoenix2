from dashboard.settings import DEBUG
import json
from .apps import APP_NAME
from .forms import *
from .repo import *
from .enums import *
from .serializers import *
from app.views import PageViews as AppPageViews
from .utils import AdminUtility
from dashboard.repo import TagRepo
from dashboard.forms import AddResumeCategoryForm, AddResumeForm
from dashboard.serializers import ResumeCategorySerializer
from dashboard.forms import AddDocumentForm, AddTagForm, AddLinkForm, AddImageForm
from dashboard.serializers import TagSerializer, DocumentSerializer, LinkSerializer, GalleryPhotoSerializer
from dashboard.views import getContext as DashboardContext
from django.shortcuts import render, redirect, reverse
from django.http import Http404, JsonResponse
from django.views import View
from utility.excel import ReportWorkBook, ReportSheet
from django.contrib.auth.decorators import login_required


TEMPLATE_ROOT = 'projectmanager/'
TUTORIAL_ROOT = TEMPLATE_ROOT+'tutorial/'

def getContext(request):
    user = request.user
    if not user.is_authenticated:
        # raise Http404
        pass
    context = DashboardContext(request)
    context['admin_utility'] = AdminUtility()
    context['search_form'] = SearchForm()
    return context


class TutorialViews(View):
    def home(self, request, *args, **kwargs):
        user = request.user
        context = getContext(request)
        return render(request, TUTORIAL_ROOT+'index.html', context)

    def add_project_location(self, request, *args, **kwargs):
        user = request.user
        context = getContext(request)
        return render(request, TUTORIAL_ROOT+'add-project-location.html', context)

    def add_project(self, request, *args, **kwargs):
        user = request.user
        context = getContext(request)
        return render(request, TUTORIAL_ROOT+'add-project.html', context)


class BasicViews(View):

    def tag(self, request, pk, *args, **kwargs):
        tag_id = pk
        tag = TagRepo(user=request.user).tag(tag_id=tag_id)
        pages = tag.pages.all().filter(app_name=APP_NAME)
        # print(pages)
        # print(100*'#')
        context = getContext(request)
        context['search_for'] = tag.title
        context['pages'] = pages
        return render(request, 'dashboard/'+'search.html', context)

    def search(self, request, *args, **kwargs):
        if request.method == 'POST':
            search_form = SearchForm(request.POST)
            if search_form.is_valid():
                search_for = search_form.cleaned_data['search_for']
                context = getContext(request)
                context['search_for'] = search_for
                context['pages'] = ManagerPageRepo(
                    user=request.user).search(search_for=search_for)
                return render(request, TEMPLATE_ROOT+'search.html', context)

    def home(self, request, *args, **kwargs):
        user = request.user
        context = getContext(request)
        projects = ProjectRepo(user=user).list_roots()
        context['projects'] = projects
        contractors = ContractorRepo(user=user).list()
        organizationunits = OrganizationUnitRepo(user=user).list_roots()
        context['organizationunits'] = organizationunits
        context['contractors'] = contractors
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form'] = AddProjectForm()
        if user.has_perm(APP_NAME+'.add_materialwarehouse'):
            context['add_materialwarehouse_form'] = AddMaterialWareHouseForm()
        if user.has_perm(APP_NAME+'.add_contracotr'):
            context['add_contracotr_form'] = AddContractorForm()
        materialwarehouses = MaterialWareHouseRepo(user=user).list()
        materialwarehouses_s = json.dumps(
            MaterialWareHouseSerializer(materialwarehouses, many=True).data)
        context['materialwarehouses_s'] = materialwarehouses_s
        projects_s = json.dumps(ProjectSerializer(projects, many=True).data)
        context['projects_s'] = projects_s
        contractors_s = json.dumps(
            ContractorSerializer(contractors, many=True).data)
        context['contractors_s'] = contractors_s
        return render(request, TEMPLATE_ROOT+'index.html', context)

    def organizationunits(self, request, *args, **kwargs):
        context = getContext(request)
        organization_units = OrganizationUnitRepo(
            user=request.user).list_roots()
        context['organization_units'] = organization_units
        context['organization_units_s'] = json.dumps(
            OrganizationUnitSerializer(organization_units, many=True).data)
        return render(request, TEMPLATE_ROOT+'org-units.html', context)

    def organizationchart(self, request, *args, **kwargs):
        context = getContext(request)
        organization_units = OrganizationUnitRepo(user=request.user).list()
        organization_units_s = OrganizationUnitSerializer(
            organization_units, many=True).data
        context['organization_units_s'] = json.dumps(organization_units_s)
        return render(request, TEMPLATE_ROOT+'org-chart.html', context)

    def archive_documents(self, request, *args, **kwargs):
        user = request.user
        context = getContext(request)
        if user.has_perm(APP_NAME+'.add_document'):
            context['add_document_form'] = AddArchiveDocumentForm()
        archive_documents = ArchiveDocumentRepo(user=user).list_roots()
        archive_documents_s = json.dumps(
            ArchiveDocumentSerializer(archive_documents, many=True).data)
        context['archive_documents_s'] = archive_documents_s
        return render(request, TEMPLATE_ROOT+'archive-documents.html', context)


class PageViews(View):

    def getManagerPageContext(self, request, page, *args, **kwargs):
        if page is None and not DEBUG:
            raise Http404
        context = getContext(request)
        context['add_tag_form'] = AddTagForm()
        context['add_link_form'] = AddLinkForm()
        context['add_document_form'] = AddDocumentForm()
        context['add_image_form'] = AddImageForm()
        context['images_s'] = json.dumps(
            GalleryPhotoSerializer(page.images.all(), many=True).data)
        context['tags_s'] = json.dumps(
            TagSerializer(page.tags.all(), many=True).data)
        context['links_s'] = json.dumps(
            LinkSerializer(page.links.all(), many=True).data)
        context['documents_s'] = json.dumps(
            DocumentSerializer(page.documents.all(), many=True).data)
        return context

    def materialwarehouse(self, request, pk, *args, **kwargs):
        user = request.user
        materialwarehouse_id = pk
        material_warehouse_repo = MaterialWareHouseRepo(user=user)
        materialwarehouse = material_warehouse_repo.materialwarehouse(
            materialwarehouse_id=materialwarehouse_id)
        context = self.getManagerPageContext(request, materialwarehouse)
        context['page_type'] = 'انبار متریال'
        context['page'] = materialwarehouse
        material_in_stocks = material_warehouse_repo.list_materials_in_stock(
            materialwarehouse_id=materialwarehouse_id)
        material_in_stocks_s = json.dumps(
            MaterialInStockSerializer(material_in_stocks, many=True).data)
        context['material_in_stocks_s'] = material_in_stocks_s
        context['organizationunit'] = materialwarehouse
        context['materialwarehouse'] = materialwarehouse
        context['projects_s'] = "[]"
        context['organizationunits_s'] = json.dumps(
            OrganizationUnitSerializer(materialwarehouse.childs(), many=True).data)

        if user.has_perm(APP_NAME+'.add_organizationunit'):
            context['add_organizationunit_form'] = AddOrganizationUnitForm()
        if user.has_perm(APP_NAME+'.add_employee'):
            context['add_employee_form'] = AddEmployeeForm()
        context['roles_s'] = json.dumps(list(x for x in EmployeeEnum))
        employees_s = json.dumps(EmployeeSerializer(
            materialwarehouse.employee_set.all(), many=True).data)
        context['employees_s'] = employees_s

        return render(request, TEMPLATE_ROOT+'material-warehouse.html', context)

    def material(self, request, pk, *args, **kwargs):
        user = request.user
        material_id = pk
        material_repo = MaterialRepo(user=user)
        material = material_repo.material(material_id=material_id)
        context = self.getManagerPageContext(request, material)
        context['page_type'] = 'متریال'
        context['page'] = material
        context['material'] = material
        return render(request, TEMPLATE_ROOT+'material.html', context)

    def presentation(self, request, pk, *args, **kwargs):
        page_id = pk
        user = request.user
        page = ManagerPageRepo(user=user).page(page_id=page_id)
        context = AppPageViews().getPageContext(request=request, page=page)

        # context=self.getManagerPageContext(request,page=page)
        context['page'] = page
        return render(request, 'material/page.html', context)

    def archivedocument(self, request, pk, *args, **kwargs):
        archivedocument_id = pk
        user = request.user
        archivedocument = ArchiveDocumentRepo(user=user).archivedocument(
            archivedocument_id=archivedocument_id)
        context = self.getManagerPageContext(request, page=archivedocument)
        context['archivedocument'] = archivedocument
        context['page'] = archivedocument
        context['page_type'] = 'سند آرشیو شده'
        return render(request, TEMPLATE_ROOT+'archive-document.html', context)

    def guantt(self, request, pk, *args, **kwargs):
        user = request.user
        context = {}
        project = ProjectRepo(user=user).project(project_id=pk)
        context['projects_s'] = json.dumps(
            ProjectSerializer(project.childs(), many=True).data)
        context['project'] = project
        return render(request, TEMPLATE_ROOT+'guantt.html', context)

    def project(self, request, pk, *args, **kwargs):
        project_id = pk
        user = request.user
        project = ProjectRepo(user=user).project(project_id=project_id)
        context = self.getManagerPageContext(request=request, page=project)
        context['events_s'] = json.dumps(EventSerializer(
            project.events.order_by('-event_date'), many=True).data)
        context['contractors_s'] = json.dumps(
            ContractorSerializer(project.contractors.all(), many=True).data)
        context['project'] = project
        context['page'] = project

        assignments_s = json.dumps(AssignmentSerializer(
            project.project_assignments.all(), many=True).data)
        context['assignments_s'] = assignments_s

        material_requests_s = json.dumps(MaterialRequestSerializer(
            project.material_requests(), many=True).data)
        context['material_requests_s'] = material_requests_s

        organizationunits_s = json.dumps(OrganizationUnitSerializer(
            project.organization_units.all(), many=True).data)
        context['organizationunits_s'] = organizationunits_s
        projects_s = json.dumps(ProjectSerializer(
            project.childs(), many=True).data)
        context['projects_s'] = projects_s
        context['edit_project_timing_form'] = EditProjectTimingForm()
        if user.has_perm(APP_NAME+'.change_project'):
            context['add_location_form'] = AddLocationForm()
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form'] = AddProjectForm()
        context['page_type'] = 'پروژه'
        return render(request, TEMPLATE_ROOT+'project.html', context)

    def event(self, request, pk, *args, **kwargs):
        event_id = pk
        user = request.user
        event = EventRepo(user=user).event(event_id=event_id)
        context = self.getManagerPageContext(request, page=event)
        context['event'] = event
        context['page'] = event
        context['page_type'] = 'رویداد'
        return render(request, TEMPLATE_ROOT+'event.html', context)

    def assignment(self, request, pk, *args, **kwargs):
        assignment_id = pk
        user = request.user
        assignment = AssignmentRepo(user=user).assignment(
            assignment_id=assignment_id)
        context = self.getManagerPageContext(request, page=assignment)
        context['assignment'] = assignment
        context['page'] = assignment
        context['page_type'] = 'تکلیف'
        return render(request, TEMPLATE_ROOT+'assignment.html', context)

    def organizationunit(self, request, pk, *args, **kwargs):
        organizationunit_id = pk
        user = request.user
        organizationunit = OrganizationUnitRepo(user=user).organizationunit(
            organizationunit_id=organizationunit_id)
        context = self.getManagerPageContext(
            request=request, page=organizationunit)
        context['organizationunit'] = organizationunit
        context['page'] = organizationunit
        if user.has_perm(APP_NAME+'.add_organizationunit'):
            context['add_organizationunit_form'] = AddOrganizationUnitForm()
        if user.has_perm(APP_NAME+'.add_employee'):
            context['add_employee_form'] = AddEmployeeForm()
        context['roles_s'] = json.dumps(list(x for x in EmployeeEnum))
        employees_s = json.dumps(EmployeeSerializer(
            organizationunit.employee_set.all(), many=True).data)
        context['employees_s'] = employees_s

        projects_s = json.dumps(ProjectSerializer(
            organizationunit.project_set.all(), many=True).data)
        context['projects_s'] = projects_s

        context['organizationunits_s'] = json.dumps(
            OrganizationUnitSerializer(organizationunit.childs(), many=True).data)
        context['page_type'] = 'واحد سازمانی'
        return render(request, TEMPLATE_ROOT+'org-unit.html', context)

    def contractor(self, request, pk, *args, **kwargs):
        contractor_id = pk
        user = request.user
        contractor = ContractorRepo(user=user).contractor(
            contractor_id=contractor_id)
        context = self.getManagerPageContext(request=request, page=contractor)
        context['contractor'] = contractor
        context['page'] = contractor
        context['page_type'] = 'پیمانکار'
        return render(request, TEMPLATE_ROOT+'contractor.html', context)


class DownloadViews(View):

    def get_page(self, request, pk, *args, **kwargs):
        user = request.user
        page_id = pk
        page = ManagerPageRepo(user=user).page(page_id=page_id)
        lines_s = page.links.values('title')
        report_work_book = ReportWorkBook()
        report_work_book.sheets.append(ReportSheet(
            data=lines_s, table_headers=None, title='سفارش شماره '+str(page_id)))
        response = report_work_book.to_excel()
        return response


class EmployeeViews(View):

    def employee(self, request, pk, *args, **kwargs):
        user = request.user
        employee_id = pk
        employee = EmployeeRepo(user=user).employee(employee_id=employee_id)
        if employee is None:
            raise Http404
        context = getContext(request=request)
        selected_profile = employee.profile
        context['body_class'] = 'profile-page'
        context['selected_profile'] = selected_profile

        if selected_profile is not None:
            context['add_resume_category_form'] = AddResumeCategoryForm()
            context['add_resume_form'] = AddResumeForm()
        resumecategories = selected_profile.resumecategory_set.all()
        resumecategories_s = json.dumps(
            ResumeCategorySerializer(resumecategories, many=True).data)
        context['resumecategories_s'] = resumecategories_s

        context['employee'] = employee
        return render(request, TEMPLATE_ROOT+'employee.html', context)


class MaterialRequestViews(View):

    def materialrequest(self, request, pk, *args, **kwargs):
        user = request.user
        context = getContext(request)
        materialrequest_id = pk
        materialrequest = MaterialRequestRepo(user=user).materialrequest(
            materialrequest_id=materialrequest_id)
        materialrequest_s = json.dumps(
            MaterialRequestSerializer(materialrequest).data)
        # print(materialrequest_s)
        context['materialrequest_s'] = materialrequest_s
        signaturestatuses_s = json.dumps(list(x for x in SignatureStatusEnum))
        context['signaturestatuses_s'] = signaturestatuses_s
        context['do_signature_form'] = DoSignatureForm()
        context['signatures_s'] = json.dumps(MaterialRequestSignatureSerializer(
            materialrequest.signatures(), many=True).data)
        return render(request, TEMPLATE_ROOT+'material-request.html', context)

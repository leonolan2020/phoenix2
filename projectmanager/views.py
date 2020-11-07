from django.shortcuts import render,redirect,reverse
from django.views import View
from .apps import APP_NAME
from django.http import Http404,JsonResponse
from dashboard.views import getContext as DashboardContext
from .repo import *
from .serializers import *
from .forms import *
from dashboard.forms import AddDocumentForm,AddTagForm,AddLinkForm,AddImageForm
import json
from utility.excel import ReportWorkBook,ReportSheet
from dashboard.serializers import TagSerializer,DocumentSerializer,LinkSerializer,GalleryPhotoSerializer
from .utils import AdminUtility
TEMPLATE_ROOT='projectmanager/'
def getContext(request):
    user=request.user
    if not user.is_authenticated:
        raise Http404
    context=DashboardContext(request)
    context['admin_utility']=AdminUtility()
    context['search_form']=SearchForm()
    return context

class BasicViews(View):
    def search(self,request,*args, **kwargs):
        if request.method=='POST':
            search_form=SearchForm(request.POST)
            if search_form.is_valid():
                search_for=search_form.cleaned_data['search_for']
                context=getContext(request)
                context['search_for']=search_for
                context['pages']=ManagerPageRepo(user=request.user).search(search_for=search_for)
                return render(request,TEMPLATE_ROOT+'search.html',context)

    def home(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        projects=ProjectRepo(user=user).list_roots()
        context['projects']=projects
        contractors=ContractorRepo(user=user).list()
        organizationunits=OrganizationUnitRepo(user=user).list_roots()
        context['organizationunits']=organizationunits
        context['contractors']=contractors
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form']=AddProjectForm()
        if user.has_perm(APP_NAME+'.add_contracotr'):
            context['add_contracotr_form']=AddContractorForm()
        projects_s=json.dumps(ProjectSerializer(projects,many=True).data)
        context['projects_s']=projects_s
        contractors_s=json.dumps(ContractorSerializer(contractors,many=True).data)
        context['contractors_s']=contractors_s
        return render(request,TEMPLATE_ROOT+'index.html',context)


    def organizationunits(self,request,*args, **kwargs):
        context=getContext(request)
        organization_units=OrganizationUnitRepo(user=request.user).list_roots()
        context['organization_units']=organization_units
        context['organization_units_s']=json.dumps(OrganizationUnitSerializer(organization_units,many=True).data)
        return render(request,TEMPLATE_ROOT+'org-units.html',context)
  

    def organizationchart(self,request,*args, **kwargs):
        context=getContext(request)
        organization_units=OrganizationUnitRepo(user=request.user).list()
        organization_units_s=OrganizationUnitSerializer(organization_units,many=True).data
        context['organization_units_s']=json.dumps(organization_units_s)
        return render(request,TEMPLATE_ROOT+'org-chart.html',context)


         
    def archive_documents(self,request,*args, **kwargs):
        user=request.user
        context=getContext(request)
        if user.has_perm(APP_NAME+'.add_document'):
            context['add_document_form']=AddArchiveDocumentForm()
        archive_documents=ArchiveDocumentRepo(user=user).list_roots()
        archive_documents_s=json.dumps(ArchiveDocumentSerializer(archive_documents,many=True).data)
        context['archive_documents_s']=archive_documents_s
        return render(request,TEMPLATE_ROOT+'archive-documents.html',context)

class PageViews(View):
    def getManagerPageContext(self,request,page,*args, **kwargs):
        context=getContext(request)
        context['add_tag_form']=AddTagForm()
        context['add_link_form']=AddLinkForm()
        context['add_document_form']=AddDocumentForm()
        context['add_image_form']=AddImageForm()
        context['images_s']=json.dumps(GalleryPhotoSerializer(page.images.all(),many=True).data)
        context['tags_s']=json.dumps(TagSerializer(page.tags.all(),many=True).data)
        context['links_s']=json.dumps(LinkSerializer(page.links.all(),many=True).data)
        context['documents_s']=json.dumps(DocumentSerializer(page.documents.all(),many=True).data)
        return context
    def archivedocument(self,request,pk,*args, **kwargs):
        archivedocument_id=pk
        user=request.user
        archivedocument=ArchiveDocumentRepo(user=user).archivedocument(archivedocument_id=archivedocument_id)
        context=self.getManagerPageContext(request,page=archivedocument)
        context['archivedocument']=archivedocument
        context['page']=archivedocument
        context['page_type']='سند آرشیو شده'
        return render(request,TEMPLATE_ROOT+'archive-document.html',context)
    def guantt(self,request,pk,*args, **kwargs):
        user=request.user
        context={}
        project=ProjectRepo(user=user).project(project_id=pk)
        context['projects_s']=json.dumps(ProjectSerializer(project.childs(),many=True).data)
        context['project']=project
        return render(request,TEMPLATE_ROOT+'guantt.html',context)
    def project(self,request,pk,*args, **kwargs):
        project_id=pk
        user=request.user
        project=ProjectRepo(user=user).project(project_id=project_id)
        context=self.getManagerPageContext(request=request,page=project)
        context['events_s']=json.dumps(EventSerializer(project.events.order_by('-event_date'),many=True).data)
        context['contractors_s']=json.dumps(ContractorSerializer(project.contractors.all(),many=True).data)
        context['project']=project
        context['page']=project
        context['edit_project_timing_form']=EditProjectTimingForm()
        if user.has_perm(APP_NAME+'.change_project'):
            context['add_location_form']=AddLocationForm()
        if user.has_perm(APP_NAME+'.add_project'):
            context['add_project_form']=AddProjectForm()
        context['page_type']='پروژه'
        return render(request,TEMPLATE_ROOT+'project.html',context)
    def event(self,request,pk,*args, **kwargs):
        event_id=pk
        user=request.user
        event=EventRepo(user=user).event(event_id=event_id)
        context=self.getManagerPageContext(request,page=event)
        context['event']=event
        context['page']=event
        context['page_type']='رویداد'
        return render(request,TEMPLATE_ROOT+'event.html',context)
    def organizationunit(self,request,pk,*args, **kwargs):
        organizationunit_id=pk
        user=request.user
        organizationunit=OrganizationUnitRepo(user=user).organizationunit(organizationunit_id=organizationunit_id)
        context=self.getManagerPageContext(request=request,page=organizationunit)
        context['organizationunit']=organizationunit
        context['page']=organizationunit
        if user.has_perm(APP_NAME+'.add_organizationunit'):
            context['add_organizationunit_form']=AddOrganizationUnitForm()
        context['organizationunits_s']=json.dumps(OrganizationUnitSerializer(organizationunit.childs(),many=True).data)
        context['page_type']='واحد سازمانی'
        return render(request,TEMPLATE_ROOT+'org-unit.html',context)
    def contractor(self,request,pk,*args, **kwargs):
        contractor_id=pk
        user=request.user
        contractor=ContractorRepo(user=user).contractor(contractor_id=contractor_id)
        context=self.getManagerPageContext(request=request,page=contractor)
        context['contractor']=contractor
        context['page']=contractor
        context['page_type']='پیمانکار'
        return render(request,TEMPLATE_ROOT+'contractor.html',context)


class DownloadViews(View):
    def get_page(self,request,pk,*args, **kwargs):
        user=request.user
        page_id=pk
        page=ManagerPageRepo(user=user).page(page_id=page_id)
        lines_s=page.links.values('title')
        report_work_book=ReportWorkBook()
        report_work_book.sheets.append(ReportSheet(data=lines_s,table_headers=None,title='سفارش شماره '+str(page_id)))
        response=report_work_book.to_excel()    
        return response

from .apps import APP_NAME
from authentication.repo import ProfileRepo
from dashboard.enums import *
from dashboard.forms import AddResumeForm,AddResumeCategoryForm,AddTagForm,AddDocumentForm,AddCommentForm,AddLinkForm,AddImageForm
from dashboard.repo import TagRepo,SocialLinkRepo
from dashboard.serializers import ResumeCategorySerializer,TagSerializer,DocumentSerializer,CommentSerializer,LinkSerializer,GalleryPhotoSerializer
from dashboard.settings import ADMIN_URL,MEDIA_URL
from dashboard.utils import AdminUtility
from dashboard.views import getContext as DashboardContext
from django.shortcuts import render,redirect,reverse
from django.views import View
from dashboard.repo import ResumeRepo as DashboardResumeRepo
from django.http import Http404
from .repo import *
from .forms import *
from .enums import MainPicEnum
import json
TEMPLATE_ROOT='material/'




def getContext(request):
    user=request.user
    context=DashboardContext(request)
    parameter_repo=ParameterRepo(user=request.user)
    main_pic_repo=MainPicRepo(user=request.user)
    link_repo=LinkRepo(user=request.user)
    context['app']={
        'social_links':SocialLinkRepo(user=user).list_for_app(app_name=APP_NAME),
        'theme_color':parameter_repo.get(ParametersEnum.THEME_COLOR),
        'GOOGLE_API_KEY':parameter_repo.get(ParametersEnum.GOOGLE_API_KEY),
        'nav_items':link_repo.get_nav_items(),
        'about_us_short':parameter_repo.get(ParametersEnum.ABOUT_US_SHORT),
        'GOOGLE_SEARCH_CONSOLE_TAG':parameter_repo.get(ParametersEnum.GOOGLE_SEARCH_CONSOLE_TAG),
        'NAV_TEXT_COLOR':parameter_repo.get(ParametersEnum.NAV_TEXT_COLOR),
        'NAV_BACK_COLOR':parameter_repo.get(ParametersEnum.NAV_BACK_COLOR),
        'slogan':parameter_repo.get(ParametersEnum.SLOGAN),
        'logo':main_pic_repo.get(name=MainPicEnum.LOGO),
        'favicon':main_pic_repo.get(name=MainPicEnum.FAVICON),
        'loading':main_pic_repo.get(name=MainPicEnum.LOADING),
        'pretitle':parameter_repo.get(ParametersEnum.PRE_TILTE),
        'title':parameter_repo.get(ParametersEnum.TITLE),
        'address':parameter_repo.get(ParametersEnum.ADDRESS),    
        'mobile':parameter_repo.get(ParametersEnum.MOBILE),           
        'email':parameter_repo.get(ParametersEnum.EMAIL),      
        'tel':parameter_repo.get(ParametersEnum.TEL),
        'url':parameter_repo.get(ParametersEnum.URL),
        'meta_data_items':MetaDataRepo().list_for_home(),
        'our_team_title':OurTeamRepo(user=user).get_title(),
        'our_team_link':OurTeamRepo(user=user).get_link(),
    }
    context['admin_utility']=AdminUtility(app_name=APP_NAME)
    return context

class BasicViews(View):
    def contact(self,request,*args, **kwargs):
        context=getContext(request)
        user=request.user

        parameter_repo=ParameterRepo(user=request.user)
        context['GOOGLE_GPS_X']=parameter_repo.get(ParametersEnum.GOOGLE_GPS_X).value
        context['GOOGLE_GPS_Y']=parameter_repo.get(ParametersEnum.GOOGLE_GPS_Y).value
        context['location']=parameter_repo.get(ParametersEnum.LOCATION)
        context['body_class']='contact-page'
        context['add_contact_message_form']=AddContactMessageForm()
        context['contact_header']=MainPicRepo(user=user).get(MainPicEnum.CONTACT_HEADER)
        context['contact_text']=ParameterRepo(user=user).get(ParametersEnum.CONTACT_US)
        

        return render(request,TEMPLATE_ROOT+'contact.html',context)

    def about(self,request,*args, **kwargs):
        context=getContext(request)
        user=request.user
        context['body_class']='about-us'
        ourteams=OurTeamRepo(user=user).list()
        context['ourteams']=ourteams
        context['about_header']=MainPicRepo(user=user).get(MainPicEnum.ABOUT_HEADER)
        context['about_text']=ParameterRepo(user=user).get(ParametersEnum.ABOUT_US_TITLE)
        return render(request,TEMPLATE_ROOT+'about.html',context)

    def home(self,request,*args,**kwargs):
        user=request.user
        context=getContext(request)
        homesliders=HomeSliderRepo(user=user).list()
        context['homesliders']=homesliders
        features=FeatureRepo(user=user).list_for_home()
        context['features']=features
        blogs=BlogRepo(user=user).list_for_home()
        context['blogs']=blogs
        ourworks=OurWorkRepo(user=user).list_for_home()
        context['ourworks']=ourworks
        ourteams=OurTeamRepo(user=user).list()
        context['ourteams']=ourteams
        return render(request,TEMPLATE_ROOT+'index.html',context)

    def features(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'features.html',context)
    def tag(self,request,pk,*args,**kwargs):
        tag_id=pk
        tag=TagRepo(user=request.user).tag(tag_id=tag_id)
        pages=tag.pages.all()
        context=getContext(request)
        context['list_title']=tag.title
        context['pages']=pages
        context['tag']=tag
        context['meta_data_items']=[tag.title,'tag']
        context['header']=MainPicRepo(user=request.user).get(MainPicEnum.TAG_HEADER)
        return render(request,TEMPLATE_ROOT+'pages.html',context)

class ProfileViews(View):
    def profile(self,request,profile_id=0,*args,**kwargs):
        context=getContext(request)
        if profile_id==0:
            selected_profile=ProfileRepo(user=request.user).me
        else:
            selected_profile=ProfileRepo(user=request.user).get(profile_id=profile_id)
        if selected_profile is None:
            raise Http404
        context['body_class']='profile-page'
        context['selected_profile']=selected_profile

        if selected_profile is not None:
            context['add_resume_category_form']=AddResumeCategoryForm()
            context['add_resume_form']=AddResumeForm()
        resumecategories=selected_profile.resumecategory_set.all()
        resumecategories_s=json.dumps(ResumeCategorySerializer(resumecategories,many=True).data)
        context['resumecategories_s']=resumecategories_s

        return render(request,TEMPLATE_ROOT+'profile.html',context)

class ExampleViews(View):
    def all_components(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/all-components.html',context)
    def sections(self,request,*args,**kwargs):
        context=getContext(request)
        return render(request,TEMPLATE_ROOT+'examples/sections.html',context)





class PageViews(View):
    def getPageContext(self,request,page,*args, **kwargs):
        if page is None:
            raise Http404
            pass
        context=getContext(request)

        context['add_tag_form']=AddTagForm()
        context['add_link_form']=AddLinkForm()
        context['add_document_form']=AddDocumentForm()
        context['add_image_form']=AddImageForm()
        context['add_comment_form']=AddCommentForm()
        comments_s=json.dumps(CommentSerializer(page.comments.all(),many=True).data)
        context['comments_s']=comments_s
        context['images_s']=json.dumps(GalleryPhotoSerializer(page.images.all(),many=True).data)
        context['tags_s']=json.dumps(TagSerializer(page.tags.all(),many=True).data)
        context['links_s']=json.dumps(LinkSerializer(page.links.all(),many=True).data)
        context['documents_s']=json.dumps(DocumentSerializer(page.documents.all(),many=True).data)
        
        return context

    def resume(self,request,pk,*args, **kwargs):
        user=request.user
        resume=DashboardResumeRepo(user=user).resume(resume_id=pk)
        context=self.getPageContext(request=request,page=resume)        
        context['page']=resume
        context['resume']=resume
        return render(request,TEMPLATE_ROOT+'resume.html',context)
    def blog(self,request,pk,*args, **kwargs):
        user=request.user
        blog=BlogRepo(user=user).blog(blog_id=pk)
        context=self.getPageContext(request=request,page=blog)
        context['page']=blog
        context['blog']=blog
        return render(request,TEMPLATE_ROOT+'blog.html',context)
    def feature(self,request,pk,*args, **kwargs):
        user=request.user        
        feature=FeatureRepo(user=user).feature(feature_id=pk)
        context=self.getPageContext(request=request,page=feature)  
        context['page']=feature
        context['feature']=feature
        return render(request,TEMPLATE_ROOT+'feature.html',context)
    def ourwork(self,request,pk,*args, **kwargs):
        user=request.user
        ourwork=OurWorkRepo(user=user).ourwork(ourwork_id=pk)
        context=self.getPageContext(request=request,page=ourwork) 
        context['page']=ourwork
        context['ourwork']=ourwork
        return render(request,TEMPLATE_ROOT+'ourwork.html',context)

# Create your views here.

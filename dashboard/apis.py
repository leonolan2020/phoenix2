from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .constants import SUCCEED,FAILED
from .repo import *
from .forms import *
from authentication.repo import ProfileRepo
import json
from .models import Document,Icon,Tag,Page,GalleryPhoto

class ProfileViews(APIView):
    def profile_customization(self,request,*args, **kwargs): 
        if request.method=='POST':
            profile_customization_form=ProfileCustomizationForm(request.POST)
            if profile_customization_form.is_valid():
                line_key=profile_customization_form.cleaned_data['line_key']
                line_value=profile_customization_form.cleaned_data['line_value']
                user=request.user
                profile=ProfileRepo(user=user).me
                if profile is not None :
                    profile_customization=profile.profile_customization()
                    if profile_customization is None:
                        profile_customization=ProfileCustomization(profile=profile)
                        profile_customization.save()
                    profile_customization.set_value(line_key=line_key,line_value=line_value)
                    profile_customization.save()
                    return JsonResponse({'result':SUCCEED})
        return JsonResponse({'result':FAILED})

class BasicViews(APIView):    
    def my_notifications(self,request,*args, **kwargs):        
        my_notifications1=NotificationRepo(user=request.user).list_unseen()
        my_notifications_s=json.dumps(NotificationSerializer(my_notifications1,many=True).data)
        context={}
        context['my_notifications_s']=my_notifications_s
        return JsonResponse(context)





class PageViews(APIView):
    def remove_tag(self,request,*args, **kwargs):        
        if request.method=='POST':
            remove_tag_form=RemoveTagForm(request.POST)
            if remove_tag_form.is_valid():
                tag_id=remove_tag_form.cleaned_data['tag_id']
                page_id=remove_tag_form.cleaned_data['page_id']
                user=request.user
                page=PageRepo(user=user).remove_tag(page_id=page_id,tag_id=tag_id)
                if page is not None:
                    tags_s=TagSerializer(page.tags.all(),many=True).data
                    return JsonResponse({'tags':tags_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED})

    def add_tag(self,request,*args, **kwargs):        
        if request.method=='POST':
            add_tag_form=AddTagForm(request.POST)
            if add_tag_form.is_valid():
                title=add_tag_form.cleaned_data['title']
                page_id=add_tag_form.cleaned_data['page_id']
                user=request.user
                page=PageRepo(user=user).add_tag(page_id=page_id,tag_title=title)
                if page is not None:                    
                    tags=page.tags.all()                  
                    tags_s=TagSerializer(tags,many=True).data
                    return JsonResponse({'tags':tags_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED})

    def add_document(self,request,*args, **kwargs):  
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_document_form=AddDocumentForm(request.POST,request.FILES)
            if add_document_form.is_valid():
                level=3
                title=add_document_form.cleaned_data['title']
                page_id=add_document_form.cleaned_data['page_id']                
                file1=request.FILES['file1']              
                page=PageRepo(user=user).add_document(page_id=page_id,file1=file1,title=title)
                if page is not None:
                    level=4                    
                    documents=page.documents.all()                  
                    documents_s=DocumentSerializer(documents,many=True).data
                    return JsonResponse({'documents':documents_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})
    
    def add_image(self,request,*args, **kwargs):  
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_image_form=AddImageForm(request.POST,request.FILES)
            if add_image_form.is_valid():
                level=3
                image_title=add_image_form.cleaned_data['title']
                page_id=add_image_form.cleaned_data['page_id']
                image_description=add_image_form.cleaned_data['description']
                location=add_image_form.cleaned_data['location']
                
                image=request.FILES['image']              
                thumbnail=request.FILES['thumbnail']              
                page=PageRepo(user=user).add_image(page_id=page_id,image=image,thumbnail=thumbnail,location=location,image_title=image_title,image_description=image_description)
                if page is not None:
                    level=4                    
                    images=page.images.all()                  
                    images_s=GalleryPhotoSerializer(images,many=True).data
                    return JsonResponse({'images':images_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})


    def add_resume_category(self,request,*args, **kwargs):  
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_resume_category_form=AddResumeCategoryForm(request.POST)
            if add_resume_category_form.is_valid():
                level=3
                title=add_resume_category_form.cleaned_data['title']
                profile_id=add_resume_category_form.cleaned_data['profile_id']
                
                resume_category=ResumeCategoryRepo(user=user).add(profile_id=profile_id,title=title)
                if resume_category is not None:
                                      
                    resume_category_s=ResumeCategorySerializer(resume_category).data
                    return JsonResponse({'resume_category':resume_category_s,'result':SUCCEED})

        return JsonResponse({'result':FAILED,'level':level})
    def add_resume(self,request,*args, **kwargs):  
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_resume_form=AddResumeForm(request.POST)
            if add_resume_form.is_valid():
                level=3
                title=add_resume_form.cleaned_data['title']
                category_id=add_resume_form.cleaned_data['category_id']
                app_name=add_resume_form.cleaned_data['app_name']
                
                resume=ResumeRepo(user=user).add(app_name=app_name,category_id=category_id,title=title)
                if resume is not None:
                                      
                    resume_s=ResumeSerializer(resume).data
                    return JsonResponse({'resume':resume_s,'result':SUCCEED})

        return JsonResponse({'result':FAILED,'level':level})

    def add_link(self,request,*args, **kwargs):  
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_link_form=AddLinkForm(request.POST)
            if add_link_form.is_valid():
                level=3
                title=add_link_form.cleaned_data['title']
                url=add_link_form.cleaned_data['url']
                page_id=add_link_form.cleaned_data['page_id']
                
                page=PageRepo(user=user).add_link(page_id=page_id,url=url,title=title)
                if page is not None:
                    level=4                    
                    links=page.links.all()                  
                    link_s=LinkSerializer(links,many=True).data
                    return JsonResponse({'links':link_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})


    def add_comment(self,request,*args, **kwargs):
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            add_comment_form=AddCommentForm(request.POST)
            if add_comment_form.is_valid():
                level=3
                text=add_comment_form.cleaned_data['text']
                page_id=add_comment_form.cleaned_data['page_id']                
                comments=CommentRepo(user=user).add(page_id=page_id,text=text)
                if comments is not None:                    
                    comments_s=CommentSerializer(comments,many=True).data
                    return JsonResponse({'comments':comments_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})
    
    def delete_comment(self,request,*args, **kwargs):
        level=1  
        user=request.user
        profile=ProfileRepo(user=user).me
        
        if request.method=='POST' and profile is not None:
            level=2
            delete_comment_form=DeleteCommentForm(request.POST)
            if delete_comment_form.is_valid():
                level=3
                comment_id=delete_comment_form.cleaned_data['comment_id']
                comments=CommentRepo(user=user).delete(comment_id=comment_id)
                if comments is not None:                    
                    comments_s=CommentSerializer(comments,many=True).data
                    return JsonResponse({'comments':comments_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})

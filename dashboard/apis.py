from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .constants import SUCCEED,FAILED
from .repo import *
from .forms import *
from authentication.repo import ProfileRepo
import json
from .models import Document,Icon,Tag,Page

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
                page=PageRepo(user=user).page(page_id=page_id)
                tag=TagRepo(user=user).tag(tag_id=tag_id)
                if page is not None and tag is not None:
                    page.tags.remove(tag)  
                    page.save()
                    tags=page.tags.all()                  
                    tags_s=TagSerializer(tags,many=True).data
                    return JsonResponse({'tags':tags_s,'result':SUCCEED})

        return JsonResponse({'result':FAILED})

    def add_tag(self,request,*args, **kwargs):        
        if request.method=='POST':
            add_tag_form=AddTagForm(request.POST)
            if add_tag_form.is_valid():
                title=add_tag_form.cleaned_data['title']
                page_id=add_tag_form.cleaned_data['page_id']
                user=request.user
                page=PageRepo(user=user).page(page_id=page_id)
                if page is not None:
                    tag=TagRepo(user=user).get_by_title(title=title)
                    if tag is None:
                        icon=Icon(icon_title='tag',icon_fa='fa fa-tag')
                        icon.save()
                        tag=Tag(title=title,icon=icon)
                        tag.save()
                    page.tags.add(tag)  
                    page.save()
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
                print(request.FILES)
                print(200*'#')
                file1=request.FILES['file1']              
                page=PageRepo(user=user).page(page_id=page_id)
                if page is not None:
                    level=4
                    document=Document(profile=profile,title=title,icon_title='tag',icon_material='get_app',file=file1)
                    document.save()
                    page.documents.add(document)  
                    page.save()
                    documents=page.documents.all()                  
                    documents_s=DocumentSerializer(documents,many=True).data
                    return JsonResponse({'documents':documents_s,'result':SUCCEED})
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
                
                page=PageRepo(user=user).page(page_id=page_id)
                if page is not None:
                    level=4
                    link=Link(profile_adder=profile,title=title,icon_title='tag',icon_material='link',url=url)
                    link.save()
                    page.links.add(link)  
                    page.save()
                    links=page.links.all()                  
                    link_s=LinkSerializer(links,many=True).data
                    return JsonResponse({'links':link_s,'result':SUCCEED})
        return JsonResponse({'result':FAILED,'level':level})

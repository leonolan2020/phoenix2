from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import *
from .constants import SUCCEED,FAILED
from .repo import *
from .forms import *
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

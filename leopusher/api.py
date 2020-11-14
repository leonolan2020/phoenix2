from rest_framework.views import View
from .forms import *
from dashboard.constants import SUCCEED,FAILED
from django.http import JsonResponse
from .repo import PusherChannelEventRepo
from .serializers import *
class BasicViews(View):
    def get_messages(self,request,*args, **kwargs):
        user=request.user
        log=1
        if request.method=='POST':
            log=2
            get_messages_form=GetMessagesForm(request.POST)
            if get_messages_form.is_valid():
                log=3
                last_id=get_messages_form.cleaned_data['last_id']
                result=PusherChannelEventRepo(user=user).get_last_messages(last_id=last_id)
                print(result)
                print(400*'#')
                messages=result['messages']
                has_more=result['has_more']
                messages_s=MessageSerializer(messages,many=True).data
                return JsonResponse({'result':SUCCEED,'has_more':has_more,'messages':messages_s})
        return JsonResponse({'result':FAILED,'log':log})



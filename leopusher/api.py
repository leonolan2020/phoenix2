from rest_framework.views import View
from .forms import *
from dashboard.constants import SUCCEED,FAILED
from django.http import JsonResponse
from .repo import PusherChannelEventRepo
from .serializers import *
class ChannelViews(View):
    def send_message(self,request,*args, **kwargs):
        user=request.user
        log=1
        if request.method=='POST':
            log=2
            send_message_form=SendMessageForm(request.POST)
            if send_message_form.is_valid():
                log=3
                text=send_message_form.cleaned_data['text']
                channelevent_id=send_message_form.cleaned_data['channelevent_id']
                message=PusherChannelEventRepo(user=request.user).add_message(text=text,channelevent_id=channelevent_id)                                
                if message is not None:
                    message_s=MessageSerializer(message).data
                    message.send(message_s)
                    return JsonResponse({'result':SUCCEED,'message':message_s})
        return JsonResponse({'result':FAILED,'log':log})


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
                
                messages=result['messages']
                has_more=result['has_more']
                messages_s=MessageSerializer(messages,many=True).data
                return JsonResponse({'result':SUCCEED,'has_more':has_more,'messages':messages_s})
        return JsonResponse({'result':FAILED,'log':log})



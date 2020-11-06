from rest_framework.views import APIView
from django.http import JsonResponse
from dashboard.constants import SUCCEED,FAILED
from .repo import *
from .forms import *
class BasicViews(APIView):
    def add_contact_message(self,request,*args, **kwargs):
        if request.method=='POST':
            add_contact_message_form=AddContactMessageForm(request.POST)
            if add_contact_message_form.is_valid():
                full_name=add_contact_message_form.cleaned_data['full_name']
                email=add_contact_message_form.cleaned_data['email']
                mobile=add_contact_message_form.cleaned_data['mobile']
                subject=add_contact_message_form.cleaned_data['subject']
                message=add_contact_message_form.cleaned_data['message']
                contact_message=ContactMessageRepo(user=request.user).add(full_name=full_name,email=email,mobile=mobile,subject=subject,message=message)
                if contact_message is not None:
                    return JsonResponse({'result':SUCCEED})
        return JsonResponse({'result':FAILED})

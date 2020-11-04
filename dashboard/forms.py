from django import forms
from .settings import SITE_URL
from .apps import APP_NAME
class AddNotificationForm(forms.Form):
    name=forms.CharField(max_length=50,required=True)
    salary=forms.IntegerField(required=True)
    city=forms.CharField(max_length=50,required=True)
    country=forms.CharField(max_length=50,required=True)

class SearchForm(forms.Form):
    action=f'{SITE_URL}{APP_NAME}/search/'
    search_for=forms.CharField(max_length=50, required=True)

class RemoveTagForm(forms.Form):
    tag_id=forms.IntegerField(required=True)
    page_id=forms.IntegerField(required=True)

class AddTagForm(forms.Form):
    title=forms.CharField(max_length=50,required=True)
    page_id=forms.IntegerField(required=True)
    
class ProfileCustomizationForm(forms.Form):
    line_key=forms.CharField(max_length=50,required=True)
    line_value=forms.CharField(max_length=50,required=True)


class AddLinkForm(forms.Form):
    page_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=50,required=True)
    url=forms.CharField(max_length=2000,required=True)

class AddDocumentForm(forms.Form):
    page_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)

class AddCommentForm(forms.Form):
    reply_to=forms.IntegerField(required=False)
    text=forms.CharField( max_length=200, required=True)
    object_id=forms.IntegerField(required=True)
    object_type=forms.CharField(required=True,max_length=30)
class AddImageForm(forms.Form):
    page_id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=100,required=True)
    description=forms.CharField(max_length=100,required=True)
    location=forms.CharField(max_length=100,required=True)

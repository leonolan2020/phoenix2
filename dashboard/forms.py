from django import forms

class AddNotificationForm(forms.Form):
    name=forms.CharField(max_length=50,required=True)
    salary=forms.IntegerField(required=True)
    city=forms.CharField(max_length=50,required=True)
    country=forms.CharField(max_length=50,required=True)


class RemoveTagForm(forms.Form):
    tag_id=forms.IntegerField(required=True)
    page_id=forms.IntegerField(required=True)

class AddTagForm(forms.Form):
    title=forms.CharField(max_length=50,required=True)
    page_id=forms.IntegerField(required=True)
from django import forms

class AddNotificationForm(forms.Form):
    name=forms.CharField(max_length=50,required=True)
    salary=forms.IntegerField(required=True)
    city=forms.CharField(max_length=50,required=True)
    country=forms.CharField(max_length=50,required=True )
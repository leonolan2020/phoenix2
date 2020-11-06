from django import forms

class AddContactMessageForm(forms.Form):    
    full_name=forms.CharField(max_length=50, required=False)
    mobile=forms.CharField(max_length=50, required=False)
    email=forms.CharField(max_length=50, required=False)
    subject=forms.CharField(max_length=50, required=True)
    message=forms.CharField(max_length=500, required=True)
    
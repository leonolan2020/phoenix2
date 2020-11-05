from django import forms

class AddContactMessageForm(forms.Form):    
    fname=forms.CharField(max_length=50, required=True)
    lname=forms.CharField(max_length=50, required=True)
    email=forms.CharField(max_length=50, required=True)
    subject=forms.CharField(max_length=50, required=True)
    message=forms.CharField(max_length=500, required=True)
    
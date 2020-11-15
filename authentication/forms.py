from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(max_length=50, required=True)
    password=forms.CharField(max_length=150, required=True)
    back_url=forms.CharField(max_length=150, required=False)

class ResetPasswordForm(forms.Form):
    username=forms.CharField(required=True,max_length=200,widget=forms.TextInput(attrs={'class':'form-control leo-farsi mt-3','placeholder':'موبایل','type':'tel'}))
    old_password=forms.CharField(max_length=150, required=False)
    new_password=forms.CharField(max_length=150, required=True)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50, required=True)
    password=forms.CharField(max_length=150, required=True)
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)

class UploadProfileImageForm(forms.Form):
    profile_id=forms.IntegerField(required=True)
    image=forms.ImageField(required=True)
  

class UploadProfileHeaderForm(forms.Form):
    profile_id=forms.IntegerField(required=True)
    header_image=forms.ImageField(required=True)
  
  
class EditProfileForm(forms.Form):
    profile_id=forms.IntegerField(required=True)
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)
    mobile=forms.CharField(max_length=50, required=False)
    address=forms.CharField(max_length=50, required=False)
    slogan=forms.CharField(max_length=50, required=False)
    bio=forms.CharField(max_length=500, required=False)
    address=forms.CharField(max_length=100, required=False)
    postal_code=forms.CharField(max_length=50, required=False)
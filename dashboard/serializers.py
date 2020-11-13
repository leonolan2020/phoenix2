from rest_framework import serializers
from .models import OurWork,Comment,Blog,Link,Notification,Tag,Document,GalleryPhoto,Resume,ResumeCategory
from authentication.models import Profile
from authentication.serializers import ProfileSerializer

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resume
        fields=['id','get_icon_tag','get_edit_url','get_absolute_url','color','title','thumbnail','short_description','description','image','persian_date_added_tag']

class ResumeCategorySerializer(serializers.ModelSerializer):
    resumes=ResumeSerializer(many=True)
    class Meta:
        model=ResumeCategory
        fields=['id','resumes','title','get_icon_tag']

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','category','icon','color','get_edit_url','title','thumbnail','short_description','description','image','persian_date_added_tag','get_absolute_url']


class OurWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=OurWork
        fields=['id','category','icon','color','get_edit_url','title','thumbnail','short_description','description','image','persian_date_added_tag','get_absolute_url']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields=['id','title','url','get_link']      


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','title','get_absolute_url','get_projectmanager_url','get_link']


class DocumentSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=Document
        fields=['id','get_link','profile','title','get_download_url']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','text','profile_id','profile_name','persian_date_added','persian_date_added_tag','profile_image','profile_get_absolute_url']
      

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=['id','title','url','get_absolute_url','icon','body','seen','date_added','color']

class GalleryPhotoSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=GalleryPhoto
        fields=['id','image','profile','get_absolute_url','get_edit_url','persian_date_added','thumbnail','image_description','image_title','location']      


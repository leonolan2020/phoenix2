from rest_framework import serializers
from .models import Comment,Blog,Link,Notification,Tag,Document,GalleryPhoto
from authentication.models import Profile
from authentication.serializers import ProfileSerializer

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields=['id','pretitle','icon','color','title','short_desc','description','image','persian_date_added','get_absolute_url']

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Link
        fields=['id','title','url','get_link']      


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields=['id','title','get_absolute_url','get_link']


class DocumentSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=Document
        fields=['id','get_link','profile','title','get_download_url']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['id','text','profile_id','profile_name','persian_date_added','persian_date_added_tag','profile_image']
      

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields=['id','title','url','get_absolute_url','icon','body','seen','date_added','color']

class GalleryPhotoSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=GalleryPhoto
        fields=['id','image','profile','get_absolute_url','get_edit_url','persian_date_added','thumbnail','image_description','image_title','location']      


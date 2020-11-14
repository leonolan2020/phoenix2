from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Message,ProfileChannelEvent,PusherChannel,PusherBeam,PusherChannelEvent
from authentication.serializers import ProfileSerializer


class MessageSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer(read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'persian_date_added', 'profile','channel_event_id', 'text']
class PusherChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PusherChannel
        fields = ['id', 'channel_name', 'key', 'cluster']
class PusherBeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=PusherBeam
        fields=['id','name','instanse_id','interests']
    
class PusherChannelEventSerializer(serializers.ModelSerializer):
    channel=PusherChannelSerializer(read_only=True)
    messages=MessageSerializer(many=True)
    class Meta:
        model=PusherChannelEvent
        fields=['id','title','channel','event_name','messages'] 
class ProfileChannelEventSerializer(serializers.ModelSerializer):
    channel_event=PusherChannelEventSerializer(read_only=True)
    class Meta:
        model=ProfileChannelEvent
        fields=['id','channel_event']  



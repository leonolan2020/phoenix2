from utility.persian import PersianCalendar
from django.db import models
from django.utils.translation import gettext as _
from .enums import PusherChannelNameEnum
from django.shortcuts import reverse
from pusher import Pusher
from .constants import MESSAGES_PAGE_SIZE
import json
import requests
class PusherChannelEvent(models.Model):
    title=models.CharField(_("title"), max_length=50)
    channel=models.ForeignKey("PusherChannel", verbose_name=_("channel"), on_delete=models.CASCADE)
    event_name=models.CharField(_("event"), max_length=50)
    def messages(self,page=1,all=False,*args, **kwargs):
        if all:
            return Message.objects.filter(channelevent=self).order_by('-id')
        else:
            start=(page-1)*MESSAGES_PAGE_SIZE
            end=(page)*MESSAGES_PAGE_SIZE
            return Message.objects.filter(channelevent=self).order_by('-id')[start:end]
    class Meta:
        verbose_name = _("ChannelEvent")
        verbose_name_plural = _("ChannelEvents")
    
    def __str__(self):
        return self.channel.channel_name+' : ' +self.title

    def get_absolute_url(self):
        return reverse("pusher:channel_event", kwargs={"channel_event_id": self.pk})

    def send_message(self,message):
        try:            
            pusher_client = Pusher(
                app_id=self.channel.app_id,
                key=self.channel.key,
                secret=self.channel.secret,
                cluster=self.channel.cluster,
                ssl=True
            )
            channel_name=self.channel.channel_name
            event_name=self.event_name
            pusher_client.trigger(channel_name, event_name, {'message': message})
        except :
            print('error in send message ')

class PusherChannel(models.Model):

    channel_name=models.CharField(verbose_name='channel_name',max_length=20) 
    app_id =models.CharField(verbose_name='app_id',max_length=20) 
    key = models.CharField(verbose_name='key',max_length=50)
    secret = models.CharField(verbose_name='secret',max_length=50)
    cluster =models.CharField(verbose_name='cluster',max_length=20,default='us2') 
    def __str__(self):
        return self.channel_name+' : '+str(self.key)

    class Meta:
        verbose_name = _("Channel")
        verbose_name_plural = _("Channels")
    def get_absolute_url(self):
        return reverse("pusher:channel", kwargs={"channel_id": self.pk})
    

class PusherBeam(models.Model):
    name=models.CharField(_("name"), max_length=50)
    instance_id=models.CharField(_("instanse_id"), max_length=100)
    authorization=models.CharField(_("authorization"), max_length=200)
  

    class Meta:
        verbose_name = _("PusherBeam")
        verbose_name_plural = _("PusherBeams")

    def __str__(self):
        return self.name

class PusherBeamInterest(models.Model):
    beam=models.ForeignKey("PusherBeam", verbose_name=_("beam"), on_delete=models.CASCADE)
    interest=models.CharField(_("interest"), max_length=50)
    def send_notification(self,title,body):            
        headers={'Content-Type': 'application/json','Authorization': self.beam.authorization}
        url='https://'+self.beam.instance_id+'.pushnotifications.pusher.com/publish_api/v1/instances/'+self.beam.instance_id+'/publishes'
        data= '{"interests":["'+self.interest+'"],"fcm":{"notification":{"title":"'+title+'","body":"'+body+'"}}}'
        response=requests.post(url,data.encode('utf-8'),headers=headers)  
        return response
    class Meta:
        verbose_name = _("PusherBeamInterest")
        verbose_name_plural = _("PusherBeamInterests")

    def __str__(self):
        return self.beam.name+" @ "+self.interest

    def get_absolute_url(self):
        return reverse("PusherBeamInterest_detail", kwargs={"pk": self.pk})

class ProfileChannelEvent(models.Model):
    profile=models.ForeignKey("authentication.Profile", verbose_name=_("profile"), on_delete=models.CASCADE)
    channel_event=models.ForeignKey("PusherChannelEvent", verbose_name=_("channel_event"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = _("ProfileChannelEvent")
        verbose_name_plural = _("ProfileChannelEvents")

    def __str__(self):
        return f'{self.channel_event} -> {self.profile.name()}'

    def get_absolute_url(self):
        return reverse("ProfileChannel_detail", kwargs={"pk": self.pk})
 


class Message(models.Model):
    channelevent=models.ForeignKey("PusherChannelEvent", verbose_name=_("کانال"), on_delete=models.CASCADE)
    profile=models.ForeignKey("authentication.Profile", verbose_name=_("پروفایل"), on_delete=models.CASCADE)
    text=models.TextField(_("متن پیام"))
    date_added=models.DateTimeField(_("date_added"), auto_now=False, auto_now_add=True)
    def persian_date_added(self):
        return PersianCalendar().from_gregorian(self.date_added)

    def channel_event_id(self):
        return self.channelevent.id
    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return f'{self.channelevent.channel.channel_name}@{self.channelevent.event_name}${self.profile.name()}#{self.text}'

    def get_absolute_url(self):
        return reverse("Message_detail", kwargs={"pk": self.pk})

    def send(self,message_s):
        channelevent=self.channelevent
        try:            
            pusher_client = Pusher(
                app_id=channelevent.channel.app_id,
                key=channelevent.channel.key,
                secret=channelevent.channel.secret,
                cluster=channelevent.channel.cluster,
                ssl=True
            )
            channel_name=channelevent.channel.channel_name
            event_name=channelevent.event_name
            pusher_client.trigger(channel_name, event_name, {'message':message_s})
        except :
            print(self.channelevent.channel.channel_name)
            print('error in send message ')
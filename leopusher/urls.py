
from django.contrib import admin
from django.urls import path,include
from . import views,api
 
app_name='pusher'
urlpatterns = [
    path('',views.IndexView.as_view(),name='home'),
    path('beam/',views.BeamView.as_view(),name='beam'),
    path('channel/',views.BeamView.as_view(),name='channel'),
    path('get_messages/',api.ChannelViews().get_messages,name='get_messages'),
    path('channels/',views.IndexView().channels,name='channels'),
    path('channel/<int:channel_id>/',views.IndexView().channels,name='channel'),
    path('channel_event/<int:channel_event_id>',views.IndexView().channels,name='channel_event'),
    path('send_beam/',views.BeamView().send_beam,name='send_beam'),
    path('send_channel/',views.ChannelView().send_channel,name='send_channel'),
    path('send_message/',api.ChannelViews().send_message,name='send_message'),
    path('chat/',views.ChannelView().chat,name='chat'),
    
]
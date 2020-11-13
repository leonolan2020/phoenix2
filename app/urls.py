from django.urls import path
from . import views,apis
from .apps import APP_NAME
app_name=APP_NAME
urlpatterns=[
    path('',views.BasicViews().home,name='home'),
    path('examples/all_components/',views.ExampleViews().all_components,name='all_components'),
    path('examples/sections/',views.ExampleViews().sections,name='sections'),
    path('pages/profile/',views.ProfileViews().profile,name='profile'),
    path('pages/profile/<int:profile_id>/',views.ProfileViews().profile,name='selected_profile'),
    path('features/',views.BasicViews().features,name='features'),
    path('blogs/',views.BasicViews().blogs,name='blogs'),
    path('ourworks/',views.BasicViews().ourworks,name='ourworks'),
    path('ourteam/<int:pk>/',views.BasicViews().features,name='ourteam'),
    path('resume/<int:pk>/',views.PageViews().resume,name='resume'),
    path('tag/<int:pk>/',views.BasicViews().tag,name='tag'),
    path('contact/',views.BasicViews().contact,name='contact'),
    path('about/',views.BasicViews().about,name='about'),
    path('blog/<int:pk>/',views.PageViews().blog,name='blog'),
    path('ourwork/<int:pk>/',views.PageViews().ourwork,name='ourwork'),
    path('feature/<int:pk>/',views.PageViews().feature,name='feature'),
    path('add_contact_message/',apis.BasicViews().add_contact_message,name='add_contact_message'),

]


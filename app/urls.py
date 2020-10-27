from django.urls import path
from . import views
from .apps import APP_NAME
app_name=APP_NAME
urlpatterns=[
    path('',views.BasicViews().home,name='home'),
    path('examples/all_components/',views.ExampleViews().all_components,name='all_components'),
    path('examples/sections/',views.ExampleViews().sections,name='sections'),
    path('pages/profile/',views.ProfileViews().profile,name='profile'),
    path('pages/profile/<int:profile_id>/',views.ProfileViews().profile,name='selected_profile'),
    path('features/',views.BasicViews().features,name='features'),
    path('ourteam/<int:pk>/',views.BasicViews().features,name='ourteam'),
    path('tag/<int:pk>/',views.BasicViews().features,name='tag'),
]


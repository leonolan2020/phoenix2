from django.urls import path
from . import views
from .apps import APP_NAME
app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('projectmanager/add_project_location/',views.ProjectManagerTutorials().add_project_location,name='add_project_location'),
]

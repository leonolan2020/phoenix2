from .apps import APP_NAME
from django.urls import path
from . import views

app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('project/<int:pk>/',views.PageViews().project,name='project'),
    path('add_project/',views.ApiViews().add_project,name='add_project'),
    
    
]

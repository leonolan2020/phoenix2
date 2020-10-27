from .apps import APP_NAME
from django.urls import path
from . import views

app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('project/<int:pk>/',views.PageViews().project,name='project'),
    path('contractor/<int:pk>/',views.PageViews().contractor,name='contractor'),
    path('organiazationunit/<int:pk>/',views.PageViews().organiazationunit,name='organiazationunit'),
    path('event/<int:pk>/',views.PageViews().event,name='event'),
    path('add_project/',views.ApiViews().add_project,name='add_project'),
    path('add_contractor/',views.ApiViews().add_contractor,name='add_contractor'),
    
    
]

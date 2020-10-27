from .apps import APP_NAME
from django.urls import path
from . import views
from . import apis

app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('search/',views.BasicViews().search,name='search'),
    path('project/<int:pk>/',views.PageViews().project,name='project'),
    path('contractor/<int:pk>/',views.PageViews().contractor,name='contractor'),
    path('organiazationunit/<int:pk>/',views.PageViews().organiazationunit,name='organiazationunit'),
    path('event/<int:pk>/',views.PageViews().event,name='event'),
    path('add_project/',apis.PageViews().add_project,name='add_project'),
    path('add_contractor/',apis.PageViews().add_contractor,name='add_contractor'),
    path('tag/<int:pk>/',views.PageViews().project,name='tag'),
    
    
    
]

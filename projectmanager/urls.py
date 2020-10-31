from .apps import APP_NAME
from django.urls import path
from . import views
from . import apis

app_name=APP_NAME
urlpatterns = [
    path('',views.BasicViews().home,name='home'),
    path('archivedocuments/',views.BasicViews().archive_documents,name='archivedocuments'),
    path('search/',views.BasicViews().search,name='search'),
    path('guantt/<int:pk>/',views.PageViews().guantt,name='guantt'),
    path('project/<int:pk>/',views.PageViews().project,name='project'),
    path('contractor/<int:pk>/',views.PageViews().contractor,name='contractor'),
    path('organiazationunit/<int:pk>/',views.PageViews().organiazationunit,name='organiazationunit'),
    path('event/<int:pk>/',views.PageViews().event,name='event'),
    path('add_project/',apis.PageViews().add_project,name='add_project'),
    path('add_location/',apis.PageViews().add_location,name='add_location'),
    path('add_event/',apis.PageViews().add_event,name='add_event'),
    path('add_contractor/',apis.PageViews().add_contractor,name='add_contractor'),
    path('tag/<int:pk>/',views.PageViews().project,name='tag'),
    path('archivedocument/<int:pk>/',views.PageViews().archivedocument,name='archivedocument'),
    path('download_page/<int:pk>/',views.DownloadViews().get_page,name='download_page'),
    
    
]

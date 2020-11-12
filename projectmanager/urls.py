from .apps import APP_NAME
from django.urls import path
from . import views
from . import apis

app_name = APP_NAME
urlpatterns = [
	path('', views.BasicViews().home, name='home'),
	path('tutorial/', views.TutorialViews().home, name='tutorial'),
	path('archivedocuments/', views.BasicViews().archive_documents,name='archivedocuments'),
	path('organizationunits/', views.BasicViews().organizationunits,name='organizationunits'),
	path('organization_chart/', views.BasicViews().organizationchart,name='organizationchart'),
	path('search/', views.BasicViews().search, name='search'),
	path('assignment/<int:pk>/', views.PageViews().assignment, name='assignment'),
	path('employee/<int:pk>/', views.EmployeeViews().employee, name='employee'),
	path('material/<int:pk>/', views.PageViews().material, name='material'),
	# path('materialcategory/<int:pk>/', views.PageViews().materialcategory, name='materialcategory'),
	path('materialwarehouse/<int:pk>/', views.PageViews().materialwarehouse, name='materialwarehouse'),
	# path('materialbrand/<int:pk>/', views.PageViews().materialbrand, name='materialbrand'),
	path('presentation/<int:pk>/', views.PageViews().presentation, name='presentation'),
	path('guantt/<int:pk>/', views.PageViews().guantt, name='guantt'),
	path('project/<int:pk>/', views.PageViews().project, name='project'),
	path('materialrequest/<int:pk>/', views.MaterialRequestViews().materialrequest, name='materialrequest'),
	path('organizationunit/<int:pk>/',views.PageViews().organizationunit, name='organizationunit'),
	path('contractor/<int:pk>/', views.PageViews().contractor, name='contractor'),
	path('organizationunit/<int:pk>/',views.PageViews().organizationunit, name='organizationunit'),
	path('event/<int:pk>/', views.PageViews().event, name='event'),
	path('do_signature/', apis.PageViews().do_signature, name='do_signature'),
	path('add_project/', apis.PageViews().add_project, name='add_project'),
	path('add_location/', apis.PageViews().add_location, name='add_location'),
	path('add_document/', apis.PageViews().add_document, name='add_document'),
	path('add_organizationunit/', apis.PageViews().add_organizationunit,name='add_organizationunit'),
	path('add_event/', apis.PageViews().add_event, name='add_event'),
	path('add_contractor/', apis.PageViews().add_contractor, name='add_contractor'),
	path('add_materialwarehouse/', apis.PageViews().add_materialwarehouse, name='add_materialwarehouse'),
	path('edit_project_timing/', apis.PageViews().edit_project_timing,name='edit_project_timing'),
	path('tag/<int:pk>/', views.BasicViews().tag, name='tag'),
	path('archivedocument/<int:pk>/',views.PageViews().archivedocument, name='archivedocument'),
	path('download_page/<int:pk>/',views.DownloadViews().get_page, name='download_page'),
	path('add_employee/', apis.PageViews().add_employee,name='add_employee'),

	path('tutorial/add_project_location/', views.TutorialViews().add_project_location,name='tutorial_add_project_location'),
	path('tutorial/add_project/', views.TutorialViews().add_project,name='tutorial_add_project'),


]

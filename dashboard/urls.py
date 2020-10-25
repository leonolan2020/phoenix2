from django.urls import path
from . import views
from .apps import APP_NAME
from app import views as app_views
app_name=APP_NAME
urlpatterns=[
path('',views.BasicViews().home,name='home'),
path('pages/timeline/',views.PagesViews().timeline,name='pages_timeline'),
path('components/notifications/',views.ComponentsViews().notifications,name='components_notifications'),
path('components/buttons/',views.ComponentsViews().buttons,name='components_buttons'),
path('components/panels/',views.ComponentsViews().panels,name='components_panels'),
path('components/alerts/',views.ComponentsViews().alerts,name='components_alerts'),
path('calendar/',views.BasicViews().calendar,name='calendar'),
path('wizard/',views.BasicViews().wizard,name='wizard'),
path('widgets/',views.BasicViews().widgets,name='widgets'),
path('charts/',views.BasicViews().charts,name='charts'),
path('tables/regular/',views.TablesViews().regular,name='tables_regular'),
path('blog/<int:pk>/',app_views.PageViews().blog,name='blog'),
path('ourwork/<int:pk>/',app_views.PageViews().ourwork,name='ourwork'),
path('feature/<int:pk>/',app_views.PageViews().feature,name='feature'),
path('notification/<int:pk>/',app_views.PageViews().feature,name='notification'),
path('notifications/',app_views.PageViews().feature,name='notifications'),
]
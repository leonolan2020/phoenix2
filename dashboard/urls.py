from django.urls import path
from . import views
from .apps import APP_NAME

app_name=APP_NAME
urlpatterns=[
path('',views.BasicView().home,name='home'),
path('pages/timeline/',views.PagesView().timeline,name='pages_timeline'),
path('components/notifications/',views.ComponentsView().notifications,name='components_notifications'),
path('components/buttons/',views.ComponentsView().buttons,name='components_buttons'),
path('components/panels/',views.ComponentsView().panels,name='components_panels'),
path('components/alerts/',views.ComponentsView().alerts,name='components_alerts'),
path('calendar/',views.BasicView().calendar,name='calendar'),
path('wizard/',views.BasicView().wizard,name='wizard'),
path('widgets/',views.BasicView().widgets,name='widgets'),
path('charts/',views.BasicView().charts,name='charts'),
path('login/',views.AuthenticationView().login,name='login'),
path('tables/regular/',views.TablesView().regular,name='tables_regular'),
]
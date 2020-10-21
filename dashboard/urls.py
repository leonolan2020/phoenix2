from django.urls import path
from . import views
from .apps import APP_NAME

app_name=APP_NAME
urlpatterns=[
path('',views.BasicView().home,name='home'),
path('pages/timeline/',views.PagesView().timeline,name='timeline'),
path('components/buttons/',views.ComponentsView().buttons,name='buttons'),
path('components/panels/',views.ComponentsView().panels,name='panels'),
]
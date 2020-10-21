from django.urls import path
from . import views
from .apps import APP_NAME

app_name=APP_NAME
urlpatterns=[
path('',views.BasicView().home,name='home'),
path('pages/timeline/',views.PagesView().timeline,name='timeline'),
path('components/buttons/',views.ComponentsView().buttons,name='buttons'),
path('components/panels/',views.ComponentsView().panels,name='panels'),
path('components/alerts/',views.ComponentsView().alerts,name='alerts'),
path('calendar/',views.BasicView().calendar,name='calendar'),
path('wizard/',views.BasicView().wizard,name='wizard'),
path('widgets/',views.BasicView().widgets,name='widgets'),
path('charts/',views.BasicView().charts,name='charts'),
]
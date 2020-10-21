from django.urls import path
from . import views
urlpatterns=[
path('',views.BasicView().home,name='home'),
]
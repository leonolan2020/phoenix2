from django.urls import path
from . import views
from .apps import APP_NAME

app_name=APP_NAME
urlpatterns=[
path('login/',views.AuthenticationView().login,name='login'),
path('logout/',views.AuthenticationView().logout,name='logout'),
]
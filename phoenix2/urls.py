from django.contrib import admin
from django.urls import path,include


# from django.conf import settings
from .settings import MEDIA_URL,MEDIA_ROOT,STATIC_URL,STATIC_ROOT,DEBUG
from django.views.static import serve 
from django.conf.urls import url


urlpatterns = [
    path('',include('authentication.urls')),


    
    path('',include('app.urls')),
    path('phoenix2/',include('app.urls')),
    path('phoenix_v1/',include('app.urls')),


    path('market/',include('market.urls')),
    path('pusher/',include('leopusher.urls')),
    path('authentication/',include('authentication.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('app/fa/',include('app.urls')),
    path('app/en/',include('app_en.urls')),
    path('projectmanager/',include('projectmanager.urls')),

    path('admin/', admin.site.urls),



    url(r'^static/(?P<path>.*)$', serve,{'document_root': STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': MEDIA_ROOT}),

    url('favicon.ico', serve,{'document_root': MEDIA_ROOT}),
]


SERVER_ON_HEROKU=False
if SERVER_ON_HEROKU:
    from django.conf.urls.static import static
    urlpatterns=urlpatterns+static(STATIC_URL, document_root=STATIC_ROOT)

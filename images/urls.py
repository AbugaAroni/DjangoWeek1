from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='Welcome'),
    re_path('search/', views.search_results, name='search_results'),
    re_path('singleimage/(\d+)',views.singleimage,name ='View image'),
    re_path('singlelocation/(\d+)',views.singlelocation,name ='View images from Location'),        
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

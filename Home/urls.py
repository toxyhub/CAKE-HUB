from django.urls import path
from . import views
from .feed import cakeupdate

urlpatterns = [
    
    path('test/',views.apex),
    path('',views.index, name='home'),
    path('login/',views.log,name='logi'),
    path('register/',views.reg,name='regi'),
    path('logout/',views.logout),
    path('srh/',views.search, name='search'),
    path('autocom/',views.autocom,name='auto'),
    path('feed/',cakeupdate()),   
]
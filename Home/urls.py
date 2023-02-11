from django.urls import path
from . import views

urlpatterns = [
    
    path('test/',views.apex),
    path('',views.index),
    path('login/',views.log,name='logi'),
    path('register/',views.reg,name='regi'),
    path('logout/',views.logout)
]
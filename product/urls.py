from django.urls import path
from . import views

urlpatterns = [

    #path('',views.details,name='details')
    #path('',views.details,name='details'),       MAIN
    path('',views.details2,name='details'),
    path('cmt/',views.commentarea,name='cmtpage'),
    
]
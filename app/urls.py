from django.conf.urls import url,include
from django.contrib import admin
from app.views import RegisterView,FirstView
from app import views
#from django.contrib.auth import views as auth_views



urlpatterns = [
	
    
    #url(r'^adminhome/',AdHome.as_view(),name='adminhome'),
    url(r'^register/',RegisterView.as_view(),name='register'),
    url(r'^login/',views.login,name='login'),
    url(r'^first/',FirstView.as_view(),name='first'),
]

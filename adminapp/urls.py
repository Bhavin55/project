from django.conf.urls import url,include
from django.contrib import admin
from adminapp.views import AdHome,AdListView,AdDeleteView,AdVehicleListView,AdVehicleDeleteView
from adminapp import views
#from django.contrib.auth import views as auth_views



urlpatterns = [
	
    url(r'^adminhome/',AdHome.as_view(),name='adminhome'),
    url(r'^adminlist/',AdListView.as_view(),name='adminlist'),
    url(r'^adminvehiclelist/',AdVehicleListView.as_view(),name='adminvehiclelist'),
    #url(r'^adminvechiledelete/(?P<pk>[0-9]+)/$',AdVechileDeleteView.as_view(),name='adminvechiledelete'),

    url(r'^admindelete/(?P<pk>[0-9]+)/$',AdDeleteView.as_view(),name='admindelete'),
]

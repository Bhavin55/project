from django.conf.urls import url,include
from django.contrib import admin
from customerapp.views import HomeView,VehicleView,VehicleListView,VehicleUpdateView,VehicleDeleteView,CuVehicleListView#,PaymentView,Success,Failure
from customerapp import views


from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
#from django.contrib.auth import views as auth_views


from customerapp import views

app_name = "customerapp"


urlpatterns = [
	
    url(r'^home/',HomeView.as_view(),name='home'),
    url(r'^vehicle/',VehicleView.as_view(),name='vehicle'),
    url(r'^vehiclelist/',VehicleListView.as_view(),name='vehiclelist'),
    url(r'^vehicleupdate/(?P<pk>[a-z A-Z 0-9]+)/$',VehicleUpdateView.as_view(),name='vehicleupdate'),
    url(r'^vehicledelete/(?P<pk>[a-z A-Z 0-9]+)/$',VehicleDeleteView.as_view(),name='vehicledelete'),
	
	url(r'^customervehiclelist/',CuVehicleListView.as_view(),name='customervehiclelist'),

	#url(r'^payments/',PaymentView.as_view(),name='payments'),


	url(r'^payment/$', views.payment, name="payment"),
    url(r'^payment/success$', views.payment_success, name="payment_success"),
    url(r'^payment/failure$', views.payment_failure, name="payment_failure"),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
#if settings.DEBUG:
#urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
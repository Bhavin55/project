from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,FormView,View,DeleteView,View
from django.contrib.auth.models import User

from customerapp.forms import VehicleForm
from customerapp.models import VehicleModel
#from django.contrib.auth.decorators import user_passes_test



#payment



from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
import logging, traceback
import customerapp.constants as constants
import customerapp.config as config
import hashlib
import requests
from random import randint
from django.views.decorators.csrf import csrf_exempt




# Create your views here.
class HomeView(TemplateView):
	"""docstring for MainView"""
	template_name='home.html'


class PaymentView(TemplateView):
	"""docstring for MainView"""
	template_name='payment.html'


class VehicleView(CreateView):
	template_name="vehicle.html"
	model=VehicleModel
	form_class=VehicleForm
	success_url='success'

class VehicleListView(ListView):

	model=VehicleModel

	template_name='vehiclelist.html'


class CuVehicleListView(ListView):
	"""docstring for CuVehicleListView"""
	template_name='customervehiclelist.html'
	def get_queryset(self):
		logged_user=self.request.user
		print(logged_user)
		queryset = VehicleModel.objects.filter(user=logged_user)
		return queryset


		

#	vehicles_id = VehicleModel.objects.get(username='queryset')





	#vehicle_id=VehicleModel.objects.get(user=queryset)


	#def get(self,request,):
	#	m_id=pk
	#	vehicle_id=VehicleModel.objects.get(id=m_id)
	#	context={
	#		'vehicle_id':vehicle_id,
	#	}	
	#	return render(request,self.template_name,context)


class VehicleUpdateView(UpdateView):
	"""docstring for VechileUpdateView"""
	model=VehicleForm
	form_class=VehicleForm
	template_name="vehicleupdate.html"
	success_url='/home/'



class VehicleDeleteView(DeleteView):
	"""docstring for VehicleDeleteView"""
	template_name="vehicledelete.html"
	model = VehicleModel
	success_url='/home/'

	
#payment
#class Success(View):
#	template_name='success.html'

#class Failure(View):
#	template_name='failure.html'


def payment(request):   
    data = {}
    txnid = get_transaction_id()
    hash_ = generate_hash(request, txnid)
    hash_string = get_hash_string(request, txnid)
    # use constants file to store constant values.
    # use test URL for testing
    data["action"] = constants.PAYMENT_URL_LIVE 
    data["amount"] = float(constants.PAID_FEE_AMOUNT)
    data["productinfo"]  = constants.PAID_FEE_PRODUCT_INFO
    data["key"] = config.KEY
    data["txnid"] = txnid
    data["hash"] = hash_
    data["hash_string"] = hash_string
    
    data["service_provider"] = constants.SERVICE_PROVIDER
    data["furl"] = request.build_absolute_uri(reverse("customerapp:payment_failure"))
    data["surl"] = request.build_absolute_uri(reverse("customerapp:payment_success"))
    
    return render(request, "payment.html", data)        
    
# generate the hash
def generate_hash(request, txnid):
    try:
        # get keys and SALT from dashboard once account is created.
        # hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
        hash_string = get_hash_string(request,txnid)
        generated_hash = hashlib.sha512(hash_string.encode('utf-8')).hexdigest().lower()
        return generated_hash
    except Exception as e:
        # log the error here.
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None

# create hash string using all the fields
def get_hash_string(request, txnid):
    hash_string = config.KEY+"|"+txnid+"|"+"10.00"+"|"+constants.PAID_FEE_PRODUCT_INFO+"|"
    hash_string += "alaina"+"|"+"test@test.com"+"|" 
    hash_string += "||||||||||"+config.SALT

    return hash_string

# generate a random transaction Id.
def get_transaction_id():
    hash_object = hashlib.sha256(str(randint(0,9999)).encode("utf-8"))
    # take approprite length
    txnid = hash_object.hexdigest().lower()[0:32]
    return txnid

# no csrf token require to go to Success page. 
# This page displays the success/confirmation message to user indicating the completion of transaction.
@csrf_exempt
def payment_success(request):
    data = {}
    return render(request, "success.html", data)

# no csrf token require to go to Failure page. This page displays the message and reason of failure.
@csrf_exempt
def payment_failure(request):
    data = {}
    return render(request, "failure.html", data)

	



		
	
		
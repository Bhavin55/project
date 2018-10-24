from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,FormView,View,DeleteView
from django.contrib.auth.models import User

from app.models import RegisterModel
from customerapp.models import VehicleModel


# Create your views here.
class AdHome(TemplateView):
	"""docstring for """
	template_name='adminhome.html'
	
	def get(self,request):
		if request.user.is_superuser:
			return render(request,self.template_name)
		else:
			return redirect('/login/')

class AdListView(ListView):
	"""docstring for adList"""
	model=RegisterModel

	template_name='adminlist.html'


class AdVehicleListView(ListView):
	"""docstring for adList"""
	model=VehicleModel

	template_name='adminvehiclelist.html'



class AdDeleteView(DeleteView):
	"""docstring for AdDeleteView"""
	template_name="admindelete.html"
	model = User
	success_url='/adminhome/'
		
class AdVehicleDeleteView(DeleteView):
	"""docstring for AdDeleteView"""
	template_name="admindelete.html"
	model = VehicleModel
	success_url='/adminhome/'

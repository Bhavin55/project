from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView,UpdateView,FormView,View
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import user_passes_test


from app.forms import UserForm,RegisterForm
from app.models import RegisterModel
from customerapp.models import VehicleModel









# Create your views here.


#class AdHome(TemplateView):

#	template_name='adminhome.html'
	
#	def get(self,request):
#		if request.user.is_superuser:
#			return render(request,self.template_name)
#		else:
#			return redirect('/login/')

class FirstView(ListView):
	"""docstring for FirstView"""
	template_name="first.html"
	model=VehicleModel

	def get(self,request):
		return render(request,self.template_name)
	

class RegisterView(FormView):
	"""docstring for CreateView"""
	template_name='register.html'
	form_class=UserForm
	model=RegisterModel



	def get(self, request, *args, **kwargs):
		self.object=None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		register_form = RegisterForm()
		return self.render_to_response(self.get_context_data(form1=user_form,form2=register_form))
	

	def post(self, request, *args, **kwargs):
		self.object=None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		register_form = RegisterForm(self.request.POST,self.request.FILES)

		if (user_form.is_valid() and register_form.is_valid()):
			return self.form_valid(user_form,register_form)
		else: 
			return self.form_invalid(user_form,register_form)

	def form_valid(self,user_form,register_form):

		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		p = register_form.save(commit=False)
		p.user = self.object
		p.save()
		return redirect('/login/')


	def form_invalid(self,user_form,register_form):
		return self.render_to_response(self.get_context_data(form1=user_form,form2=register_form)) 
#User authentiation
def login(request): 
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/adminhome/")# or your url name
         if request.user.is_staff:
             return redirect("/home/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/adminhome/")# or your url name
             if request.user.is_staff:
                 return redirect("/home/")# or your url name

         else:
             messages.error(request, 'Error wrong username/password')
     context = {}
     context['form']=form

     return render(request, 'login.html', context)

@user_passes_test(lambda u: u.is_staff)
def StaffHome(request):
     context = {}
     return render(request, 'home.html', context)

@user_passes_test(lambda u: u.is_superuser)
def AdminHome(request):
     context = {}
     return render(request, 'adminhome.html', context)

#reCaptia

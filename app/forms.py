from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.models import RegisterModel


class UserForm(UserCreationForm):
	class Meta:
		model=User
		fields=['username','first_name','last_name','email']


class RegisterForm(forms.ModelForm):
	class Meta:
		model=RegisterModel
		fields=['cus_address','cus_nation','cus_phone','cus_gender']
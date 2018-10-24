from django import forms
from customerapp.models import VehicleModel

class VehicleForm(forms.ModelForm):
	class Meta():
		model=VehicleModel
		exclude=("create_date",)
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class RegisterModel(models.Model):
	gender=(('male','male'),('female','female'),('others','others'))
	user=models.OneToOneField(User,on_delete=models.CASCADE)

	cus_address=models.CharField(max_length=20)
	cus_nation=models.CharField(max_length=20)
	cus_phone=models.IntegerField(default=10)
	cus_gender=models.CharField(max_length=20,choices=gender)
	
	def __str__(self):
		return (self.cus_address)

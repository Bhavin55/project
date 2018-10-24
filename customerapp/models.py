from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class VehicleModel(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,default='user.username')

    Ve_type=models.CharField(max_length=20)
    Ve_accomadate=models.IntegerField(default=0)
    Ve_model=models.IntegerField(default=0)
    Ve_price=models.IntegerField(default=0)
    Ve_photo=models.ImageField(upload_to='media/pic/')
    Ve_file=models.FileField(upload_to='media/file/')
    created_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.Ve_type


from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerprofilePic/',null=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_name(self):
        return self.user.id
    def _str_(self):
        return self.user.first_name

class Tasks(models.Model):
    name=models.CharField(max_length=40)
    date=models.DateField()
    def __str__(self):
        return self.name



from django import forms
from django.contrib.auth.models import User
from . import models


from django.core.validators import RegexValidator
from .models import User, Customer


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }

from django.core.validators import MinValueValidator, MaxValueValidator

class CustomerForm(forms.ModelForm):
    address = forms.CharField(validators=[RegexValidator(r'^[a-zA-Z\s]*$', 'Only characters are allowed.')])
    mobile = forms.IntegerField(
        validators=[
            MinValueValidator(1000000000, 'Mobile number must be 10 digits.'),
            MaxValueValidator(9999999999, 'Mobile number must be 10 digits.')
        ]
    )

    class Meta:
        model = Customer
        fields = ['address', 'mobile', 'profile_pic']
   
   
class TasksForm(forms.ModelForm):
        class Meta:
            model=models.Tasks
            fields=['name','date']

            
    

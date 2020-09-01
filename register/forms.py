from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserModel


class RegisterForm(UserCreationForm):#registration form
    class Meta:
        model = User
        fields = ("username", "email","password1","password2","first_name","last_name")


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model=UserModel
        labels = {
            "Office_Phone": "Office Phone",
            "Mobile_Phone":"Mobile Phone",
            "LinkedIn_address":"LinkedIn address"
        }
        exclude=('user',)

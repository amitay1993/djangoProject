from django import forms
from django.forms import ModelForm
from contacts.models import ContactModel,UserModel


class Login(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=UserModel
        fields="__all__"


class NewContact(ModelForm):#maybe  we should  change  it to model form
    # first_name = forms.CharField(label='First Name:', max_length=32)
    # last_name = forms.CharField(label='Last Name:', max_length=32)
    # email = forms.EmailField(label='Email:')
    # phone = forms.CharField(label='Phone Number:', max_length=10)
    class Meta:
        model=ContactModel
        exclude=("user",)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm,UserProfileInfoForm



# Create your views here.

def register(response):
    if response.method == "POST":
        django_form = RegisterForm(response.POST)#django User
        profile_form=UserProfileInfoForm(response.POST)#our user

        if django_form.is_valid() and profile_form.is_valid() :
            user=django_form.save()
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
        else:
            return HttpResponse("Invalid")
            # print("**********************")
            # n=form.cleaned_data['username']
            # print("**********************")
            # form.save()
        return redirect("/")
    else:
        form = RegisterForm()
        profile_form=UserProfileInfoForm()
    return render(response, "register/register.html", {'form': form,'ourform':profile_form})


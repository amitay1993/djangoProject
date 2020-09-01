from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import UserModel, ContactModel, User
from .forms import Login, NewContact

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect


# Create your views here.


def home(response):
    form = Login()
    if response.method == "GET":
        if response.user.is_active:
            return redirect("/myaccount")
        return render(response, "registration/login.html", {"form": form})
    else:
        if response.method == "POST":
            form = Login(response.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        login(response, user)
                        response.session['username'] = username
                        return redirect("/myaccount")  # here  we  need to send the dictinoary and puplate it
                else:
                    return render(response,"registration/login.html",{"form":form,'error':"Username and Password did not match"})


def user_login(response):
    if response.method == "POST":
        form = Login(response.POST)
        if form.is_valid():
            n = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            u = User(username=n, password=p)
            u.save()
            return HttpResponseRedirect("/%i" % u.id)
    else:
        form = Login()
    return render(response, "registration/login.html", {"form": form})


@login_required
def my_account(request):
    con = ContactModel.objects.filter(user=request.user)

    u = User.objects.get(username=request.user)
    return render(request, 'contacts/home.html', {"user": u, "contacts": con})


@login_required
def add_contact(request):
    form = NewContact()
    if request.method=="GET":
        return render(request, "contacts/add_contact.html", {"form":form})
    else:
        if request.method=="POST":
            form = NewContact(request.POST)
            if form.is_valid():
                new_user = form.save(commit=False)
                new_user.user = request.user
                new_user.save()
                return redirect("/myaccount")



@login_required
def editcontact(request,contact_id):
    contact=get_object_or_404(ContactModel,pk=contact_id)#from admin
    if request.method=="GET":
        if request.user != contact.user:
            return HttpResponse("Accsess Denied")
        form=NewContact(instance=contact)
        return render(request,"contacts/edit.html",{"contact":contact,"form":form})
    else:
        # save or delete
        form = NewContact(request.POST,instance=contact)  # since we already have a contact and we want to change we specify wich instance to change
        if "save" in request.POST:
            if form.is_valid():
                form.save()

                return redirect("/myaccount")
        else:
                if form.is_valid():
                    contact.delete()
                    return redirect("/myaccount")

@login_required
def user_logout(request):
    logout(request)
    return redirect("/")



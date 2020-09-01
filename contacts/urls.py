from django.urls import path

from . import views

urlpatterns = [
    # path("<int:id>", views.index, name="index"),
    path('', views.home, name="home"),
    path('register/login/', views.user_login, name="login"),
    path("myaccount/",views.my_account,name="my_account"),
    path("addcontact/", views.add_contact, name="add_contact"),
    path("edit/<int:contact_id>", views.editcontact, name="edit_contact"),
    path('home/', views.home, name="home"),
    path('logout/', views.user_logout, name="home"),
]

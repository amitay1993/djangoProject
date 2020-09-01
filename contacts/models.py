from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserModel(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username


class ContactModel(models.Model):#add contact form

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="contact",null=True)
    Titles = (
        ("1", "Mr"),
        ("2", "Mrs"),
        ("3", "Miss"),
        ("4", "Dr"),
        ("5", "Prof"))

    Title = models.CharField(max_length=1, choices=Titles, blank=False, default=Titles[0])
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Profession = models.CharField(max_length=128, blank=True)
    Academic_Acreditation = models.CharField(max_length=128, blank=True)
    Institution = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=50)
    Office_Phone=models.IntegerField(default=0,verbose_name="Office Phone")
    Mobile_Phone=models.IntegerField(default=0,verbose_name="Mobile Phone")
    Address = models.CharField(max_length=128, blank=True)
    LinkedIn_address=models.URLField(blank=True,verbose_name="LinkedIn address")#correspnd to the type we would specify in HTML

    def __str__(self):
        return self.first_name



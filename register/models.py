from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserModel(models.Model):

    #model calss to add adinonal info that the default user does not have
    #for ex: like titles
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Titles = (
        ("1", "Mr"),
        ("2", "Mrs"),
        ("3", "Miss"),
        ("4", "Dr"),
        ("5", "Prof"))

    Title=models.CharField(max_length=1,choices=Titles,blank=False,default=Titles[0])

    Profession=models.CharField(max_length=128,blank=True)
    Academic_Acreditation=models.CharField(max_length=128,blank=True)
    Institution=models.CharField(max_length=128,blank=True)
    Office_Phone=models.CharField(max_length=20,verbose_name="Office Phone")
    Mobile_Phone=models.IntegerField(default=0,verbose_name="Mobile Phone")
    Address=models.CharField(max_length=128,blank=True)
    LinkedIn_address=models.URLField(blank=True,verbose_name="LinkedIn address")



    def __str__(self):
        return self.user.username
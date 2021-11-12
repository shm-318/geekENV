from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# Create your models here.

class Contact(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField(max_length=200)
    ContactNo= models.PositiveBigIntegerField()
    Message = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    picture_url = models.CharField(max_length=100,null=True, blank=True)
    full_name = models.CharField(max_length=100, help_text='Help people discover your account by using the name',null=True)
    email = models.EmailField(unique=True)
    
    # last_name=None
    # first_name=None

    # Optional fields
    status = models.CharField(max_length=100,null=True,blank=True,help_text='Help people discover your account by using the name')
    college = models.CharField(max_length=30,blank=True,null=True)
    website = models.CharField(max_length=30,blank=True,null=True)
    country = models.CharField(max_length=20,blank=True,null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    gender = models.CharField(max_length=10,null=True, blank=True)
    
    def str(self):
        return self.username

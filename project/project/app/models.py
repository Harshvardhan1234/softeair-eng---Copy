from turtle import mode
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)
    # img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)



class USER_STD(models.Model):
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # img = models.ImageField(upload_to='pics')
    roll_no = models.CharField(max_length=50)
    age = models.IntegerField()


class TEMP(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
   
    
class registration1(models.Model):
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     dep_name = models.CharField(max_length=50)
     roll_no = models.CharField(max_length=50)
     address = models.CharField(max_length=100)
     gender = models.CharField(max_length=50)
     dob = models.CharField(max_length=50)
     pincode = models.CharField(max_length=50)
     resume = models.CharField(max_length=50)
     email_id = models.CharField(max_length=50)
     password = models.CharField(max_length=50)



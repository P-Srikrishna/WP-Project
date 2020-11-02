from django.db import models

# Create your models here.
class Registration1(models.Model): 
    FirstName   = models.CharField(max_length =120)
    LastName    = models.CharField(max_length =120)
    Email       = models.CharField(max_length =120)
    Password    = models.CharField(max_length =16)
    Address     = models.CharField(max_length =120)
    PhoneNumber = models.CharField(max_length =12)
    City        = models.CharField(('City'), max_length =120)
    date        = models.DateField()
    
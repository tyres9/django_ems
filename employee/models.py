from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse
from django_countries.fields import CountryField
from django.utils import timezone


class Position(models.Model):
    titles = models.CharField(max_length = 50)

    
    def __str__(self):
        return self.titles

class Employee(models.Model):   
    GENDER  = (("male", "Male"),
                ("female", "Female"),
                )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length = 20, choices = GENDER, default = 'MALE')
    address  = models.TextField()
    country = CountryField(blank_label = ('select country'),default = 'Select Country')
    cell_number = models.CharField(blank = True,max_length = 11)
    dispatch_company = models.CharField(max_length = 100)
    position = models.ForeignKey(Position, on_delete= models.CASCADE)
    date_started = models.DateField(blank = True, default = timezone.now)
 

    def __str__(self):
        return self.first_name + str(" ")+self.last_name

    def get_absolute_url(self):
       return reverse("EmployeeDetail", kwargs={"pk": self.pk})
    

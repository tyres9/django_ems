from django.db import models
from django.contrib.auth.models import User
import datetime
from django.urls import reverse


class Employee(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address  = models.TextField()
    cell_number = models.CharField(blank = True,max_length = 11)
    dispatch_company = models.CharField(max_length = 100)
    position = models.CharField(max_length = 50)
    date_started = models.DateField(blank = True)
    picture = models.ImageField(upload_to = "employee_img" )

    def __str__(self):
        return self.firstname + str(" ")+self.lastname

    def get_absolute_url(self):
        return reverse("EmployeeDetail", kwargs={"pk": self.pk})
    

from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/Employee_listview.html'
    context_object_name = 'EmployeeList'

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/Employee_detailview.html'


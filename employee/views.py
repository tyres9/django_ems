from django.shortcuts import render
from .models import Employee
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.urls import reverse



class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee/Employee_listview.html'
    context_object_name = 'EmployeeList'
    ordering = ['last_name']
    paginate_by = 1

class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/Employee_detailview.html'

class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = 'employee/Employee_updateview.html'
    fields = '__all__'
    
class EmployeeCreateView(CreateView):
    model = Employee
    #template_name = 'employee/Employee_create.html'
    fields = '__all__' 

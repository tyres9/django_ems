from django.urls import path
from .views import EmployeeListView, EmployeeDetailView

urlpatterns = [
    path('', EmployeeListView.as_view(), name = 'EmployeeList'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name = 'EmployeeDetail'),
]
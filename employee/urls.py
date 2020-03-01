from django.urls import path
from .views import EmployeeListView, EmployeeDetailView, EmployeeUpdateView,EmployeeCreateView

urlpatterns = [
    path('', EmployeeListView.as_view(), name = 'EmployeeList'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name = 'EmployeeDetail'),
    path('employee/<int:pk>/update/', EmployeeUpdateView.as_view(), name = 'EmployeeUpdate'),
    path('employee/register', EmployeeCreateView.as_view(), name = 'EmployeeCreate'),
]
from .models import Employee



class EmployeeFormUpdate(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
    

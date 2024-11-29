from django import forms
from .models import Branch,Employee


class EmployeeForm(forms.ModelForm):
    # Define the 'phone' field directly in the form to use the custom widget
 # Use CountryField instead of CharField for country selection

    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'country', 'phone']

        
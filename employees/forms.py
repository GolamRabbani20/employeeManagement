from django import forms
from django.forms import ModelForm
from .models import employeeDetails
import datetime 

class employeeForm(ModelForm):
    class Meta:
        model = employeeDetails
        fields = ('first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'photo') # For specific fields
        labels = {
            'first_name': "" ,
            'last_name': "" ,
            'email':"", 
            'mobile':"", 
            'date_of_birth':"", 
            'photo':""
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Adderss'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile Number'}), 
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Select a date'}),
        }
   
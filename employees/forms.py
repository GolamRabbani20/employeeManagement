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
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
        }
    #     date_of_birth = forms.DateField(
    #     widget=forms.DateInput(format="%d/%m/%Y",
    #                            attrs={'type': 'date',
    #                                   'min': str(datetime.datetime.now().date()),
    #                                   'max': str((datetime.datetime.now() + datetime.timedelta(days=365)).date())}),
    #     help_text='Select a date',
    #     input_formats=["%d/%m/%Y"],
    #     # validators=[validate_future_date],
    # )
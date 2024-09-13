from django.contrib import admin
from .models import employeeDetails

@admin.register(employeeDetails)
class employeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_of_birth', 'photo')

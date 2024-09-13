from django.shortcuts import render

def employeeList(request):
    return render(request, 'employees/employee_list.html', {'employees': 'Alhumdulillah! Done'})

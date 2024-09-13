from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import employeeDetails
from .forms import employeeForm
from django.core.paginator import Paginator

def employeeList(request):
    employees = employeeDetails.objects.all()
    p = Paginator(employees, 5)
    page = request.GET.get('page')
    employees = p.get_page(page)
    nums = 'a' * employees.paginator.num_pages
    return render(request, 'employees/employee_list.html', {'employees': employees, 'nums': nums})

def addEmployee(request):
    submitted = False
    if request.method == "POST":
        form = employeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_emp?submitted=True')
    else:
       form = employeeForm()
       if 'submitted' in request.GET:
           submitted = True
    return render(request, 'employees/add_employee.html', {'form': form, 'submitted': submitted})

def updateEmployee(request, employee_id):
    employee = employeeDetails.objects.get(pk=employee_id)
    form = employeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee-list')
    return render(request, 'employees/update_employee.html', {'form': form})

def deleteEmployee(request, employee_id):
    employee = employeeDetails.objects.get(pk=employee_id)
    employee.delete()
    return redirect('employee-list')

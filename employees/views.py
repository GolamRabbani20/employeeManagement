from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import employeeDetails
from .forms import employeeForm
from django.core.paginator import Paginator
from django.db.models import Q

def employeeList(request, sort_name='first_name'):
    order_by = request.GET.get('order_by', sort_name)
    employees = employeeDetails.objects.all().order_by(order_by)
    total_employees = len(employees)
    p = Paginator(employees, 5)
    page_no = request.GET.get('page')
    employees = p.get_page(page_no)
    nums = 'a' * employees.paginator.num_pages
    return render(request, 'employees/employee_list.html', {'employees': employees, 'nums': nums, 'lowerlimit':(int(page_no)*5)-4, 'upperlimit':int(page_no)*5, 'total_employees': total_employees})

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

def searchEmployee(request):
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        dob = request.GET.get('dob')
        phone = request.GET.get('phone')

        if name != '' and email != '' and dob != '' and phone != '':
            employees = employeeDetails.objects.filter((Q(first_name__icontains=name) | Q(email__icontains=email)) & (Q(date_of_birth__exact=dob) | Q(mobile__exact=phone)))
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        
        return render(request, 'employees/search.html', {})
    else:
        return render(request, 'employees/search.html', {})


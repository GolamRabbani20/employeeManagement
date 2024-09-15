from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import employeeDetails
from .forms import employeeForm
from django.core.paginator import Paginator
from django.db.models import Q

def employeeList(request, sort_name='first_name'):
    order_by = request.GET.get('order_by', sort_name)
    all_employees = employeeDetails.objects.all().order_by(order_by)
    ipp = 10
    p = Paginator(all_employees, ipp)
    page = request.GET.get('page')

    if page is None:
        page = 1
    
    page_no = int(page)
        
    # Employees per page
    employees = p.get_page(page)
    nums = 'a' * employees.paginator.num_pages

    return render(request, 'employees/employee_list.html', {'employees': employees, 'nums': nums, 'total_employees': len(all_employees), 'lowerlimit': page_no*ipp-9, 'upperlimit': page_no*ipp, 'page_no': page_no})

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
    employee = get_object_or_404(employeeDetails, pk=employee_id)
    form = employeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee-list')
    return render(request, 'employees/update_employee.html', {'form': form})

def deleteEmployee(request, employee_id):
    employee = get_object_or_404(employeeDetails, pk=employee_id)
    employee.delete()
    return redirect('employee-list')

def searchEmployee(request):
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        dob = request.GET.get('date_of_birth')
        phone = request.GET.get('phone')

        if name != '' and email != '' and dob != '' and phone != '':
            employees = employeeDetails.objects.filter(((Q(first_name__icontains=name)|Q(last_name__icontains=name)) | Q(email__icontains=email)) & (Q(date_of_birth__exact=dob) | Q(mobile__exact=phone)))
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        
        elif phone != '':
            employees = employeeDetails.objects.filter(mobile__exact=phone)
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        
        elif dob != '':
            employees = employeeDetails.objects.filter(date_of_birth__exact=dob)
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        
        elif name != '':
            employees = employeeDetails.objects.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        
        elif email != '':
            employees = employeeDetails.objects.filter(email__icontains=email)
            return render(request, 'employees/search.html', {'search':[name, email, dob, phone], 'employees':employees})
        else:
            return render(request, 'employees/search.html', {})
        
    else:
        return render(request, 'employees/search.html', {})


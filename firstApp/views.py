from django.shortcuts import render
from .models import Employee   # make sure Blog model is imported

def addAdmissions(request):
    # Static values
    values = {
        'name': 'Harish',
        'age': 30,
        'course': 'Django'
    }

    # Dynamic values from Blog model
    posts = Employee.objects.all()
    values['posts'] = posts

    return render(request, 'firstApp/add-admissions.html', values)

def viewAdmissionsReport(request):
    return  render(request, 'firstApp/admissions-report.html')

def showEmployees(request):
    employees = Employee.objects.all()   # fetch all records
    return render(request, 'firstApp/show-employees.html', {'employees': employees})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeForm



def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()   # inserts new record into DB
            return redirect('employee_list')  # redirect to list page after creation
    else:
        form = EmployeeForm()
    return render(request, 'firstApp/create_employee.html', {'form': form})


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'firstApp/employee_list.html', {'employees': employees})



def update_employee(request, pk):
    # Fetch employee by primary key (id)
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()   # Updates the record in DB
            return redirect('employee_list')  # Redirect after update
    else:
        form = EmployeeForm(instance=employee)  # Pre-fill form with existing data

    return render(request, 'firstApp/update_employee.html', {'form': form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':   # confirm deletion
        employee.delete()
        return redirect('employee_list')   # go back to list after delete
    return render(request, 'firstApp/delete_employee.html', {'employee': employee})


def searchEmployee(request):
    query = request.GET.get('q')  # get search term from URL query string
    if query:
        employees = Employee.objects.filter(name__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'firstApp/search_employee.html', {'employees': employees, 'query': query})
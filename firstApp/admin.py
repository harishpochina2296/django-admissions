from django.contrib import admin
from firstApp.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'gender', 'dno')
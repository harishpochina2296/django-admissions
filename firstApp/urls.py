from django.urls import path
 
from firstApp.views import addAdmissions
from firstApp.views import viewAdmissionsReport
from firstApp.views import showEmployees
from firstApp import views


urlpatterns = [
   
    path('addadm/', addAdmissions),
    path('viewadm/', viewAdmissionsReport),
    path('employees/',showEmployees),
    path('employee/create/', views.create_employee, name='create_employee'),
    path('employee/list', views.employee_list, name='employee_list'),  # list view
    path('employee/<int:pk>/update/', views.update_employee, name='update_employee'),
    path('employee/<int:pk>/delete/', views.delete_employee, name='delete_employee'),
    path('searchEmployee/', views.searchEmployee, name='searchEmployee'),

]  



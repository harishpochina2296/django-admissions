
# Create your models here.
from django.db import models

class Employee(models.Model):
    # id will be created automatically as primary key by Django
    id= models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    dno = models.IntegerField()  # department number

    def __str__(self):
        return f"{self.name} ({self.dno})"
from django.db import models
from app.models import EmployeeModel

class SalariedModel(models.Model):
    employee_id = models.ForeignKey(EmployeeModel)
    salary = models.IntegerField(default=15000)

    def __str__(self):
        return self.employee_id

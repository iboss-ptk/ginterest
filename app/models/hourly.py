from django.db import models
from app.models import EmployeeModel

class HourlyModel(models.Model):
    employee_id = models.ForeignKey(EmployeeModel)
    wage = models.IntegerField(default=40)

    def __str__(self):
        return self.employee_id

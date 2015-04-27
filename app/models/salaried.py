from django.db import models
from app.models import Employee

class Salaried(models.Model):
    employee_id = models.ForeignKey(Employee)
    salary = models.IntegerField(default=15000)

    def __str__(self):
        return str(self.employee_id)+' @'+str(self.salary)

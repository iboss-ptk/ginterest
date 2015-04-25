from django.db import models
from app.models import Employee

class Hourly(models.Model):
    employee_id = models.ForeignKey(Employee)
    wage = models.IntegerField(default=40)

    def __str__(self):
        return self.employee_id+' @'+self.wage

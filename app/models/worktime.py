import datetime
from django.db import models
from app.models import Employee

class Worktime(models.Model):
    DAYS_OF_WEEK = (
            ('sun','Sunday'),
            ('mon','Monday'),
            ('tue','Tuesday'),
            ('wed','Wednesday'),
            ('thu','Thursday'),
            ('fri','Friday'),
            ('sat','Saturday'),
    )
    employee_id = models.ForeignKey(Employee)
    day_of_week = models.CharField(max_length=3,choices=DAYS_OF_WEEK)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.employee_id+' - '+self.day_of_week+' @'+start_time+' - '+end_time

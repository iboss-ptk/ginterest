import datetime
from django.db import models

class CustomerGroupModel(models.Model):
    number_of_customer = models.IntegerField(default=1)
    queue_no = models.IntegerField(default=0)
    enter_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.enter_time+" ("+self.number_of_customer+")"

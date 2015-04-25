import datetime
from django.db import models
from app.models import CustomerGroupModel

class ReservationModel(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    home_tel_no = models.CharField(max_length=9)
    mobile_no = models.CharField(max_length=10)
    number_of_seat = models.IntegerField(default=1)
    reserved_time = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(CustomerGroupModel)

    def __str__(self):
        return self.firstname+" "+self.reserved_time

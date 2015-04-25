import datetime
from django.db import models
from app.models import Menu
from app.models import Orderlist
from app.models import Employee

class Order(models.Model):
    ORDER_STATUSES = (
            ('q','Queuing'),
            ('c','Being cooked'),
            ('f','Finished'),
    )
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=ORDER_STATUSES)
    comment = models.CharField(max_length=70)
    quantity = models.IntegerField(default=1)
    menu_id = models.ForeignKey(Menu)
    orderlist_id = models.ForeignKey(Orderlist)
    employee_id = models.ForeignKey(Employee)

    def __str__(self):
        return self.menu_id+" ("+self.quantity+")"

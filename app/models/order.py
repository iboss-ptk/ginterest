import datetime
from django.db import models
from app.models import MenuModel
from app.models import OrderlistModel
from app.models import EmployeeModel

class OrderModel(models.Model):
    ORDER_STATUSES = (
            ('q','Queuing'),
            ('c','Being cooked'),
            ('f','Finished'),
    )
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1,choices=ORDER_STATUSES)
    comment = models.CharField(max_length=70)
    quantity = models.IntegerField(default=1)
    menu_id = models.ForeignKey(MenuModel)
    orderlist_id = models.ForeignKey(OrderlistModel)
    employee_id = models.ForeignKey(EmployeeModel)

    def __str__(self):
        return self.menu_id+" ("+self.quantity+")"

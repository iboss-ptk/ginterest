import datetime
from django.db import models
from app.models import DTModel
from app.models import OrderListModel
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
    dtable_id = models.ForeignKey(DTableModel)
    orderlist_id = models.ForeignKey(OrderListModel)
    employee_id = models.ForeignKey(EmployeeModel)

    def __str__(self):
        return self.

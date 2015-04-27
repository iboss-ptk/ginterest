import datetime
from django.db import models
#from app.models.orderlist import Orderlist
#from app.models.menu import Menu
#from app.models.order import Order


class CustomerGroup(models.Model):
    number_of_customer = models.IntegerField(default=1)
    queue_no = models.IntegerField(default=0)
    enter_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.enter_time)+' ('+str(self.number_of_customer)+')'

    def total_income(self):
        total = 0
        orderL = Orderlist.objects.get(customergroup_id=self)
        allOrders = Order.objects.all().prefetch_related(orderL)
        for order in allOrders:
            morder = Menu.objects.all().prefetch_releated(order)
            total+= (order.quantity)*(morder.price)
        return total

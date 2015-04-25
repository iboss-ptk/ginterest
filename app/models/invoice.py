import datetime
from django.db import models
from app.models import Supplier

class Invoice(models.Model):
    INVOICE_STATUSES = (
        ('p','Pending'),
        ('o','Ordered'),
        ('d','Delivering'),
        ('f','Delivered'),
    )
    date = models.DateTimeField('date published')
    supplier_id = models.ForeignKey(Supplier)
    status = models.CharField(max_length=1,choices=INVOICE_STATUSES)

    def __str__(self):
        return self.supplier_id+" @"+self.date

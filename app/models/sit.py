from django.db import models
from app.models import DTable
from app.models import CustomerGroup

class Sit(models.Model):
    table_id = models.ForeignKey(DTable)
    customer_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return self.customer_id+" @"+self.table_id

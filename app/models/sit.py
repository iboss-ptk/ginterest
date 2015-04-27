from django.db import models
from app.models import DTable
from app.models import CustomerGroup

class Sit(models.Model):
    table_id = models.ForeignKey(DTable)
    customer_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return str(self.customer_id)+" @"+str(self.table_id)

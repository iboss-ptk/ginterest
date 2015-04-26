from django.db import models
from app.models import DTable
from app.models import CustomerGroup

class Orderlist(models.Model):
    dtable_id = models.ForeignKey(DTable)
    customergroup_id = models.ForeignKey(CustomerGroup)

    def __str__(self):
        return self.dtable_id

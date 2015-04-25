from django.db import models
from app.models import DTableModel
from app.models import CustomerGroupModel

class SitModel(models.Model):
    table_id = models.ForeignKey(DTableModel)
    customer_id = models.ForeignKey(CustomerGroupModel)

    def __str__(self):
        return self.customer_id+" @"+self.table_id

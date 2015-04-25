from django.db import models
from app.models import DTable

class Orderlist(models.Model):
    dtable_id = models.ForeignKey(DTable)

    def __str__(self):
        return self.dtable_id

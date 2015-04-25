from django.db import models
from app.models import DTableModel

class OrderlistModel(models.Model):
    dtable_id = models.ForeignKey(DTableModel)

    def __str__(self):
        return self.dtable_id

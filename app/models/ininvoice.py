from django.db import models
from app.models import Invoice
from app.models import Ingredient

class InInvoice(models.Model):
    ingredient_id = models.ForeignKey(Ingredient)
    invoice_id = models.ForeignKey(Invoice)
    quantity_bought = models.IntegerField(default=1)
    price = models.IntegerField(default=1)

    def __str__(self):
        return self.ingredient_id+"x"+self.quantity_bought+" @"+self.invoice_id+" $"+self.price

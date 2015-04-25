from django.db import models
from app.models import Menu
from app.models import Ingredient

class Recipe(models.Model):
    menu_id = models.ForeignKey(Menu)
    ingredient_id = models.ForeignKey(Ingredient)
    quantity_used = models.IntegerField(default=1)

    def __str__(self):
        return self.quantity_used+"x"+self.ingredient_id+" @"+self.menu_id

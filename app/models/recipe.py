from django.db import models
from app.models import MenuModel
from app.models import IngredientModel

class RecipeModel(models.Model):
    menu_id = models.ForeignKey(MenuModel)
    ingredient_id = models.ForeignKey(IngredientModel)
    quantity_used = models.IntegerField(default=1)

    def __str__(self):
        return self.quantity_used+"x"+self.ingredient_id+" @"+self.menu_id

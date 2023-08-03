import uuid

from django.db import models

from fresco.apps.recipes.domain.models.ingredient import Ingredient
from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.models.units import UnitsEnum
from fresco.shared.base.base_model import BaseModel


class RecipeIngredient(BaseModel):
    """
    Model that represents a relation between an ingredient and a recipe. In the relation we need to specify the amount of ingredient that the recipe has.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
    unit = models.CharField(
        max_length=10, choices=[(unit.value, unit.name) for unit in UnitsEnum]
    )

    def __str__(self):
        return f"{self.quantity} {self.unit} of {self.ingredient.name} for {self.recipe.title}"

    class Meta:
        db_table = "recipe_ingredients"

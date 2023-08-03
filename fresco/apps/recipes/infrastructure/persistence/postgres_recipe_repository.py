from typing import List

from django.db import transaction, IntegrityError

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository
from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient


class PostgresRecipeRepository(RecipeRepository):
    def create_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> bool:
        try:
            with transaction.atomic():
                recipe.save(recipe)

                for recipe_ingredient in recipe_ingredients:
                    recipe_ingredient.save()
            return True
        except IntegrityError:
            return False

    def update_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> bool:
        try:
            with transaction.atomic():
                recipe.save()

                RecipeIngredient.objects.filter(recipe=recipe).delete()

                for recipe_ingredient in recipe_ingredients:
                    recipe_ingredient.recipe = recipe
                    recipe_ingredient.save()

            return recipe
        except IntegrityError as e:
            print(str(e))
            return False

    def save(self, recipe: Recipe) -> Recipe:
        recipe.save()
        return recipe

    def get_all(self) -> List[Recipe]:
        return list(Recipe.objects.all())

    def get(self, id: str) -> Recipe | None:
        try:
            return Recipe.objects.get(id=id)
        except:
            return None

    def delete(self, recipe: Recipe):
        recipe.delete()

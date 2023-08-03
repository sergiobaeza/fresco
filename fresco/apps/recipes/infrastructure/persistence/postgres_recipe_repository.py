from typing import List

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository
from fresco.apps.recipes.domain.models.recipe import Recipe


class PostgresRecipeRepository(RecipeRepository):
    def save(recipe: Recipe) -> Recipe:
        recipe.save()
        return recipe

    def get_all() -> List[Recipe]:
        return list(Recipe.objects.all())

    def get(id: str) -> Recipe | None:
        try:
            Recipe.objects.get(id=id)
        except:
            return None

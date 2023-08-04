from typing import List
import uuid
from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository
from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient


from typing import List, Optional
from uuid import UUID


class InMemoryRecipeRepository(RecipeRepository):
    def __init__(self, recipes: List[Recipe]):
        self.recipes = recipes

    def create_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> bool:
        for iter in self.recipes:
            if str(iter.id) == str(recipe.id):
                return False
        self.recipes.append(recipe)
        return True

    def update_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> Optional[Recipe]:
        for iter in self.recipes:
            if str(iter.id) == id:
                self.recipes.remove(iter)
                self.recipes.append(recipe)
                return recipe
        return None

    def save(self, recipe: Recipe) -> Recipe:
        self.recipes.append(recipe)
        return recipe

    def get_all(self) -> List[Recipe]:
        return self.recipes

    def get(self, id: str) -> Optional[Recipe]:
        for recipe in self.recipes:
            if str(recipe.id) == str(id):
                return recipe
        return None

    def delete(self, recipe: Recipe):
        for iter in self.recipes:
            if str(iter.id) == str(recipe.id):
                self.recipes.remove(recipe)
                return
        return None

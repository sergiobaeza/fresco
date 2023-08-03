from typing import List

from injector import inject

from fresco.apps.recipes.application.schemas.recipe import RecipeIn, RecipeModifyIn
from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository


class RecipeService:
    @inject
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def create_recipe(recipe: RecipeIn) -> Recipe:
        pass

    def get_recipe(self, uuid: str) -> Recipe | None:
        return self.recipe_repository.get(uuid)

    def get_all_recipes(self) -> List[Recipe]:
        return self.recipe_repository.get_all()

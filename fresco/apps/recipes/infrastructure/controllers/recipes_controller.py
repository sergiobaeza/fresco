from typing import List
from pydantic import UUID4

from ninja.errors import HttpError

from ninja_extra import api_controller, http_get, http_post, http_put
from ninja_jwt.authentication import JWTAuth

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository

from fresco.apps.recipes.application.schemas.recipe import RecipeOut
from fresco.apps.recipes.application.services.recipes_service import RecipeService


@api_controller("/recipes")
class RecipesController:
    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    @http_get("", response=List[RecipeOut])
    def get_recipe(self):
        """
        Get all the recipes in the database with their relationship between ingredients
        """
        return self.recipe_service.get_all_recipes()

    @http_get("/{id}", response=RecipeOut)
    def get_recipe_by_id(self, id: UUID4):
        """
        Gets a recipe by his UUID
        """
        recipe = self.recipe_service.get_recipe(id)
        if not recipe:
            raise HttpError(404, "Not found")
        return recipe

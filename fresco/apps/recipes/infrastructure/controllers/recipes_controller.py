from typing import List
from pydantic import UUID4

from ninja.errors import HttpError

from ninja_extra import api_controller, http_get, http_post, http_put
from ninja_jwt.authentication import JWTAuth

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository

from fresco.apps.recipes.application.schemas.recipe import (
    RecipeOut,
    RecipeIn,
    RecipeModifyIn,
)
from fresco.apps.recipes.application.services.recipes_service import RecipeService


@api_controller("/recipes", tags=["recipes"], auth=JWTAuth())
class RecipesController:
    def __init__(self, recipe_service: RecipeService):
        self.recipe_service = recipe_service

    @http_post(
        "",
        response={201: None},
        openapi_extra={
            "responses": {
                "400": {
                    "description": "Bad request",
                },
                "401": {
                    "description": "Not authenticated",
                },
            }
        },
    )
    def create_recipe(self, payload: RecipeIn):
        """
        Creates a recipe
        """
        created = self.recipe_service.create_recipe(payload)
        if not created:
            raise HttpError(400, "Bad request")

        return 201, None

    @http_get(
        "",
        response=List[RecipeOut],
        openapi_extra={
            "responses": {
                "401": {
                    "description": "Not authenticated",
                },
            }
        },
    )
    def get_recipes(self):
        """
        Get all the recipes in the database with their relationship between ingredients
        """
        return self.recipe_service.get_all_recipes()

    @http_get(
        "/{id}",
        response=RecipeOut,
        openapi_extra={
            "responses": {
                "401": {
                    "description": "Not authenticated",
                },
                "404": {
                    "description": "Resource not found",
                },
            }
        },
    )
    def get_recipe_by_id(self, id: UUID4):
        """
        Gets a recipe by his UUID
        """
        recipe = self.recipe_service.get_recipe(id)
        if not recipe:
            raise HttpError(404, "Not found")
        return recipe

    @http_put(
        "/{id}",
        response=RecipeOut,
        openapi_extra={
            "responses": {
                "400": {
                    "description": "Bad request",
                },
                "401": {
                    "description": "Not authenticated",
                },
            }
        },
    )
    def update_recipe_by_id(self, id: UUID4, payload: RecipeModifyIn):
        """
        Gets a recipe by his UUID
        """
        recipe = self.recipe_service.update_recipe(id, payload)
        if not recipe:
            raise HttpError(400, "Bad request")
        return recipe

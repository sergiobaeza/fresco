from ninja_extra import api_controller, http_get, http_post, http_put
from ninja_jwt.authentication import JWTAuth

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository


@api_controller("/recipes", auth=JWTAuth)
class RecipesController:
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    @http_post("/upload")
    def upload_profile_pic(
        self,
    ):
        return {}

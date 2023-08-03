from typing import List

from injector import inject

from fresco.apps.recipes.application.schemas.recipe import RecipeIn, RecipeModifyIn
from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient
from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository


class RecipeService:
    @inject
    def __init__(self, recipe_repository: RecipeRepository):
        self.recipe_repository = recipe_repository

    def create_recipe(self, recipe_in: RecipeIn) -> bool:
        recipe: Recipe = Recipe(
            id=recipe_in.id,
            title=recipe_in.title,
            description=recipe_in.description,
            estimated_time=recipe_in.estimated_time,
            steps=recipe_in.steps,
            diners=recipe_in.diners,
        )
        ingredients = list()
        for recipe_ingredient in recipe_in.ingredients:
            ingredients.append(
                RecipeIngredient(
                    ingredient_id=recipe_ingredient[0],
                    quantity=recipe_ingredient[1],
                    unit=recipe_ingredient[2],
                    recipe=recipe,
                )
            )

        return self.recipe_repository.create_with_ingredients(
            recipe=recipe, recipe_ingredients=ingredients
        )

    def update_recipe(self, uuid: str, recipe_in: RecipeModifyIn) -> bool:
        recipe: Recipe = self.recipe_repository.get(uuid)
        if not recipe:
            return False

        recipe.title = recipe_in.title
        recipe.description = recipe_in.description
        recipe.estimated_time = recipe_in.estimated_time
        recipe.steps = recipe_in.steps
        recipe.diners = recipe_in.diners

        ingredients = list()
        for recipe_ingredient in recipe_in.ingredients:
            ingredients.append(
                RecipeIngredient(
                    ingredient_id=recipe_ingredient.ingredient_id,
                    quantity=recipe_ingredient.quantity,
                    unit=recipe_ingredient.unit,
                    recipe=recipe,
                )
            )
        return self.recipe_repository.update_with_ingredients(
            recipe=recipe, recipe_ingredients=ingredients
        )

    def get_recipe(self, uuid: str) -> Recipe | None:
        return self.recipe_repository.get(uuid)

    def get_all_recipes(self) -> List[Recipe]:
        return self.recipe_repository.get_all()

from typing import List

from abc import ABC, abstractmethod

from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient


class RecipeRepository(ABC):
    @abstractmethod
    def create_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> bool:
        raise NotImplemented()

    @abstractmethod
    def update_with_ingredients(
        self, recipe: Recipe, recipe_ingredients: List[RecipeIngredient]
    ) -> Recipe:
        raise NotImplemented()

    @abstractmethod
    def save(self, recipe: Recipe) -> Recipe:
        raise NotImplemented()

    @abstractmethod
    def get_all(self) -> List[Recipe]:
        raise NotImplemented()

    @abstractmethod
    def get(self, id: str) -> Recipe | None:
        raise NotImplemented()

    @abstractmethod
    def delete(self, recipe: Recipe):
        raise NotImplemented()

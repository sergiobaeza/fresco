from typing import List

from abc import ABC, abstractmethod

from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient


class RecipeIngredientRepository(ABC):
    @abstractmethod
    def save(recipe: RecipeIngredient) -> RecipeIngredient:
        raise NotImplemented()

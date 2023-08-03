from typing import List

from abc import ABC, abstractmethod

from fresco.apps.recipes.domain.models.recipe import Recipe


class RecipeRepository(ABC):
    @abstractmethod
    def save(recipe: Recipe) -> Recipe:
        raise NotImplemented()

    @abstractmethod
    def get_all() -> List[Recipe]:
        raise NotImplemented()

    @abstractmethod
    def get(id: str) -> Recipe | None:
        raise NotImplemented()

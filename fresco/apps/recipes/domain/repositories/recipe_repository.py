from typing import List

from abc import ABC, abstractmethod

from fresco.apps.recipes.domain.models.recipe import Recipe


class RecipeRepository(ABC):
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

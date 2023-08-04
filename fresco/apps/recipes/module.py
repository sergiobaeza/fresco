from injector import Binder, Module, singleton

from fresco.apps.recipes.domain.repositories.recipe_repository import RecipeRepository
from fresco.apps.recipes.infrastructure.persistence.postgres_recipe_repository import (
    PostgresRecipeRepository,
)


class RecipesDefinitionModule(Module):
    """
    Class that allows to do the dependency injection by django injector package
    """

    def configure(self, binder: Binder) -> None:
        binder.bind(RecipeRepository, to=PostgresRecipeRepository, scope=singleton)

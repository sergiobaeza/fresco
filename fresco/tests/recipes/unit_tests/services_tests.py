import uuid

from pydantic import UUID4

from fresco.apps.recipes.domain.models.recipe import Recipe
from fresco.apps.recipes.application.services.recipes_service import (
    RecipeService,
    RecipeIn,
)
from fresco.tests.recipes.helpers.repositories import InMemoryRecipeRepository


def get_recipe_service(uuid: UUID4) -> RecipeService:
    """
    Creates a recipe service and injects a inmemory repository with 1 item
    """
    repo = InMemoryRecipeRepository(
        [
            Recipe(
                id=uuid,
                title="The best recipe of the world",
                description="You will love it :P",
                estimated_time=20,
                steps=["Buy the food", "Cook it for 20 mins", "Eat it"],
                diners=20,
            )
        ]
    )
    return RecipeService(repo)


def get_recipe_service_empty_repo() -> RecipeService:
    """
    Creates a service with an empty inmemory repository
    """
    repo = InMemoryRecipeRepository([])
    return RecipeService(repo)


def test_service_create_recipe_OK():
    """
    Test that creates a new recipe
    """
    id = uuid.uuid4()
    other_id = uuid.uuid4()

    recipe = RecipeIn(
        id=id,
        title="The best recipe of the world",
        description="You will love it :P",
        estimated_time=20,
        steps=["Buy the food", "Cook it for 20 mins", "Eat it"],
        diners=20,
        ingredients=[],
    )
    service = get_recipe_service(other_id)

    assert service.create_recipe(recipe)


def test_service_create_recipe_uuid_exists_KO():
    """
    Test that tries to create a new recipe but it exists one with the same
    """
    id = uuid.uuid4()

    recipe = RecipeIn(
        id=id,
        title="The best recipe of the world",
        description="You will love it :P",
        estimated_time=20,
        steps=["Buy the food", "Cook it for 20 mins", "Eat it"],
        diners=20,
        ingredients=[],
    )
    service = get_recipe_service(id)

    assert service.create_recipe(recipe) == False


def test_service_get_recipe_uuid_exists_OK():
    """
    Test that tries to get an existing and non existing recipe in the repository
    """
    id = uuid.uuid4()
    other_id = uuid.uuid4()
    service = get_recipe_service(id)

    assert service.get_recipe(other_id) is None
    assert service.get_recipe(id) is not None


def test_service_get_all_recipes_OK():
    """
    Test that gets all the recipes from the repository
    """
    id = uuid.uuid4()
    service = get_recipe_service(id)

    assert len(service.get_all_recipes()) == 1


def test_service_get_all_recipes_none_OK():
    """
    Test that gets all the recipes from the repository when its empty
    """
    service = get_recipe_service_empty_repo()

    assert len(service.get_all_recipes()) == 0

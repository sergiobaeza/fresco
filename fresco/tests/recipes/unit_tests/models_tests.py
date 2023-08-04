import uuid

from fresco.apps.recipes.domain.models.ingredient import Ingredient
from fresco.apps.recipes.domain.models.recipe_ingredient import RecipeIngredient
from fresco.apps.recipes.domain.models.recipe import Recipe


def test_ingredient_model():
    """
    Test for creating an Ingredient model
    """
    name = "onion"
    id = uuid.uuid4()

    ingredient = Ingredient(name=name, id=id)

    assert ingredient.name == name
    assert ingredient.id == id
    assert str(ingredient) == name


def test_recipe_ingredient_model():
    """
    Test for creating a Recipe Ingredient model
    """
    id = uuid.uuid4()
    quantity = 10
    unit = "kg"

    recipe_ingredient = RecipeIngredient(id=id, quantity=quantity, unit=unit)

    assert recipe_ingredient.id == id
    assert recipe_ingredient.quantity == quantity
    assert recipe_ingredient.unit == unit


def test_recipe_model():
    """
    Test for creating a Recipe model
    """
    id = uuid.uuid4()
    title = "The best recipe of the world"
    description = "You will love it :P"
    estimated_time = 20
    steps = ["Buy the food", "Cook it for 20 mins", "Eat it"]
    diners = 20

    recipe = Recipe(
        id=id,
        title=title,
        description=description,
        estimated_time=estimated_time,
        steps=steps,
        diners=diners,
    )

    assert recipe.id == id
    assert recipe.title == title
    assert recipe.description == description
    assert recipe.estimated_time == estimated_time
    assert recipe.steps == steps
    assert recipe.diners == diners

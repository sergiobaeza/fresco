from ninja import Schema
from pydantic import UUID4, validator
from typing import List, Tuple
from datetime import datetime
from fresco.apps.recipes.domain.models.recipe_ingredient import UNIT_CHOICES
from pydantic import PositiveInt


def validate_unit(cls, unit):
    valid_choices = [x[0] for x in UNIT_CHOICES]
    if unit not in valid_choices:
        raise ValueError(
            f"Invalid unit choice. Valid choices are: {', '.join(valid_choices)}"
        )
    return unit


class Ingredient(Schema):
    id: UUID4
    name: str


class RecipeIngredientOut(Schema):
    ingredient: Ingredient
    unit: str
    quantity: PositiveInt

    unit_validator = validator("unit", allow_reuse=True)(validate_unit)


class RecipeIngredientIn(Schema):
    ingredient_id: UUID4
    unit: str
    quantity: PositiveInt

    unit_validator = validator("unit", allow_reuse=True)(validate_unit)


class BaseRecipe(Schema):
    title: str
    description: str
    estimated_time: PositiveInt
    steps: List[str]
    diners: PositiveInt = None


class RecipeOut(BaseRecipe):
    id: UUID4
    ingredients: List[RecipeIngredientOut]
    created_at: datetime
    updated_at: datetime


class RecipeModifyIn(BaseRecipe):
    ingredients: List[RecipeIngredientIn]


class RecipeIn(BaseRecipe):
    id: UUID4
    ingredients: List[RecipeIngredientIn]

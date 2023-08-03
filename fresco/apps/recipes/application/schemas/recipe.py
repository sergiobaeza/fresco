from ninja import Schema
from pydantic import UUID4
from typing import List, Tuple
from datetime import datetime
from fresco.apps.recipes.domain.models.units import UnitsEnum


class BaseRecipe(Schema):
    title: str
    description: str
    estimated_time: int
    steps: List[str]
    diners: int = None


class RecipeOut(BaseRecipe):
    id: UUID4
    ingredients: List[str]
    created_at: datetime
    updated_at: datetime


class RecipeModifyIn(BaseRecipe):
    ingredients: List[Tuple[UUID4, int, UnitsEnum]]


class RecipeIn(BaseRecipe):
    id: UUID4
    ingredients: List[Tuple[UUID4, int, UnitsEnum]]

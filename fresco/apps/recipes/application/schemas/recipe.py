from ninja import Schema
from pydantic import UUID4
from typing import List, Tuple
from datetime import datetime
from fresco.apps.recipes.domain.models.units import UnitsEnum


class BaseRecipe(Schema):
    id: UUID4
    title: str
    description: str
    estimated_time: int
    steps: List[str]
    diners: int = None


class RecipeOut(BaseRecipe):
    ingredients: List[str]
    created_at: datetime
    updated_at: datetime


class RecipeIn(BaseRecipe):
    ingredients: List[UUID4, int, UnitsEnum]

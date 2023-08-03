import uuid

from django.db import models

from fresco.shared.base.base_model import BaseModel


class Recipe(BaseModel):
    """
    Entity that represents a Recipe
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=164)
    description = models.CharField(max_length=400)
    time = models.IntegerField()
    steps = models.JSONField(default=list)
    diners = models.IntegerField(null=True)

    class Meta:
        db_table = "recipes"

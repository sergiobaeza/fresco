import uuid

from django.db import models

from fresco.shared.base.base_model import BaseModel


class Ingredient(BaseModel):
    """
    Model that represents an Ingredient like onion, tomatoes, milk...
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "ingredients"

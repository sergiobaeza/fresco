from django.contrib import admin
from django.urls import path

from ninja_extra import NinjaExtraAPI, api_controller
from ninja_jwt.controller import NinjaJWTDefaultController

from fresco.apps.recipes.infrastructure.controllers.recipes_controller import (
    RecipesController,
)

api = NinjaExtraAPI(title="Fresco Recipes", description="Simple and easy Recipes")

api.register_controllers(NinjaJWTDefaultController)
api.register_controllers(RecipesController)

urlpatterns = [path("v1/api/", api.urls)]

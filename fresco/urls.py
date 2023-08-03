from django.contrib import admin
from django.urls import path

from ninja_extra import NinjaExtraAPI, api_controller
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI(title="Fresco Recipes", description="Simple and easy Recipes")

api.register_controllers(NinjaJWTDefaultController)


urlpatterns = [path("v1/api/", api.urls)]

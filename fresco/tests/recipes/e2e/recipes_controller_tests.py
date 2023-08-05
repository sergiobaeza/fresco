import uuid

import pytest

from django.test import Client
from django.contrib.auth.models import User
from django.conf import settings

RECIPE_DATA = {
    "title": "Recipe",
    "description": "A test recipe",
    "estimated_time": 60,
    "steps": ["First step", "Second step "],
    "diners": 20,
    "id": f"{uuid.uuid4()}",
    "ingredients": [],
}


def get_api_clients():
    """
    Helper function that gives back 2 clients, one authorized and the other unauthorized
    """

    User.objects.create_user(username="stest", email="test@test", password="aaa")
    data = {"password": "aaa", "username": "stest"}
    unauthorized = Client()

    response = unauthorized.post(
        path="/v1/api/token/pair", data=data, content_type="application/json"
    )

    headers = {"HTTP_AUTHORIZATION": "Bearer " + response.json()["access"]}

    authorized = Client(**headers)

    return authorized, unauthorized


@pytest.mark.django_db(True)
def test_get_recipes_OK():
    authorized, unauthorized = get_api_clients()

    response = unauthorized.get("/v1/api/recipes")
    assert response.status_code == 401

    response = authorized.get("/v1/api/recipes")
    assert response.status_code == 200
    assert response.json()["count"] == 0


@pytest.mark.django_db(True)
def test_create_recipe_OK():
    authorized, unauthorized = get_api_clients()

    response = unauthorized.post("/v1/api/recipes")
    assert response.status_code == 401

    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201

    # Get amount of total recipes now its 1
    response = authorized.get("/v1/api/recipes")
    assert response.status_code == 200
    assert response.json()["count"] == 1


@pytest.mark.django_db(True)
def test_create_recipe_KO():
    authorized, unauthorized = get_api_clients()

    response = unauthorized.post("/v1/api/recipes")
    assert response.status_code == 401

    response = authorized.post(
        "/v1/api/recipes", data={}, content_type="application/json"
    )
    assert response.status_code == 422

    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201

    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 400


@pytest.mark.django_db(True)
def test_get_recipe_OK():
    authorized, unauthorized = get_api_clients()

    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201  # OK CREATED -> no response

    response = unauthorized.get("/v1/api/recipes/" + RECIPE_DATA["id"])
    assert response.status_code == 401

    # Create recipe and check status
    response = authorized.get("/v1/api/recipes/" + RECIPE_DATA["id"])
    assert response.status_code == 200
    response_data = response.json()

    assert response_data["id"] == RECIPE_DATA["id"]
    assert response_data["description"] == RECIPE_DATA["description"]
    assert response_data["diners"] == RECIPE_DATA["diners"]
    assert response_data["steps"] == RECIPE_DATA["steps"]
    assert response_data["title"] == RECIPE_DATA["title"]
    assert response_data["estimated_time"] == RECIPE_DATA["estimated_time"]


@pytest.mark.django_db(True)
def test_get_recipe_KO():
    authorized, unauthorized = get_api_clients()
    rnd_uuid = uuid.uuid4()
    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201

    response = unauthorized.get(f"/v1/api/recipes/{rnd_uuid}")
    assert response.status_code == 401

    # Get recipe that doesnt exist
    response = authorized.get(f"/v1/api/recipes/{rnd_uuid}")
    assert response.status_code == 404


@pytest.mark.django_db(True)
def test_update_recipe_OK():
    authorized, unauthorized = get_api_clients()
    rnd_uuid = uuid.uuid4()
    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201

    # New data for the recipe
    new_data = RECIPE_DATA
    new_data["title"] = "Updated recipe"
    new_data["description"] = "Updated description"
    new_data["estimated_time"] = 60
    new_data["steps"] = []
    new_data["diners"] = 20

    response = unauthorized.put(f"/v1/api/recipes/" + RECIPE_DATA["id"])
    assert response.status_code == 401

    # Updating the recipe
    response = authorized.put(
        f"/v1/api/recipes/" + RECIPE_DATA["id"],
        data=new_data,
        content_type="application/json",
    )
    assert response.status_code == 200

    response = authorized.get("/v1/api/recipes/" + RECIPE_DATA["id"])
    assert response.status_code == 200
    response_data = response.json()

    assert response_data["title"] == new_data["title"]
    assert response_data["description"] == new_data["description"]
    assert response_data["estimated_time"] == new_data["estimated_time"]
    assert response_data["steps"] == new_data["steps"]
    assert response_data["diners"] == new_data["diners"]
    assert response_data["id"] == new_data["id"]


@pytest.mark.django_db(True)
def test_update_recipe_KO():
    authorized, unauthorized = get_api_clients()
    rnd_uuid = uuid.uuid4()
    response = authorized.post(
        "/v1/api/recipes", data=RECIPE_DATA, content_type="application/json"
    )
    assert response.status_code == 201

    # Sending wrong payload
    response = authorized.put(
        f"/v1/api/recipes/" + RECIPE_DATA["id"],
        data={},
        content_type="application/json",
    )
    assert response.status_code == 422

    # Recipe that doesnt exist
    response = authorized.put(
        f"/v1/api/recipes/{uuid.uuid4()}",
        data=RECIPE_DATA,
        content_type="application/json",
    )
    assert response.status_code == 400

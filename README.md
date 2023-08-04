# FRESCO API Rest Project

This project is a representation of an API Rest for Recipes with CREATE, READ, and UPDATE methods.

## Features

- **JWT:** For authentication, the API provides a JWT token with HS 256 signature method. The token's lifetime is set to 5 minutes, and a refresh token is available for 24 hours.
- **Code Quality:** The code maintains a well-structured format with the help of tools like pre-commit, editorconfig, and the black linter.
- **Architecture:** The project follows a hexagonal architecture adapted to Django and pydantic schemas.
- **OpenAPI:** You can access the Swagger UI of the project at `v1/api/docs`. Additionally, the OpenAPI definition is available in the `openapi` folder.
- **Docker:** The application is dockerized to facilitate deployment.
- **Persistence Layer:** PostgreSQL is used as the database.
- **Package Management:** Poetry is used as the package manager.
- **Pagination:** Pagination is implemented for better handling of large datasets.
- **REST Approach:** The controllers are designed following the REST paradigm understanding what is a resource.
- **Tests**: The project tries to get benefit from the structure to do Unit Tests

## Project Structure

The project aims to follow the SOLID principles and the Hexagonal architecture, customized to suit the specific requirements of this project.

## Tests
The project has the models and the recipe service tested. I've used Dependency Injection to override the external persistence and used a memory one.

## Deployment
First of all rename the .env.example to .env and modify the variables if needed.

To deploy the application, you have the following options:

1. **Docker Image:** Build the Docker image and deploy it.
2. **Docker Compose:** Use Docker Compose if a database container is needed.
3. **Local Development:** For development purposes, you can run the application in a poetry environment.

### Migrating Schemas

To migrate the schemas to the database, execute the following command inside the container:

``` python
python manage.py migrate
```


### Creating a Super User

If you wish to create a superuser, use the following command:

``` python
python manage.py createsuperuser
```


Feel free to explore the project, contribute, and use it in your own applications! For detailed API documentation, refer to the Swagger UI at `/v1/api/docs`.

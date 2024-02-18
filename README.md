# fastapi-swagger-exploration

This repository serves as a learning exercise, designed to explore and implement various technologies in a practical project setting. It focuses on the use of the fastAPI web framework, together with Uvicorn, SQLAlchemy, and Swagger UI for API documentation, to build and document a web API. Through hands-on experience with Docker for containerization, Alembic for database migrations, and the uv Python package installer.

### Tech stack

[uv](https://github.com/astral-sh/uv) Python package installer. Reading: [uv: Python packaging in Rust](https://astral.sh/blog/uv).

[fastAPI](https://fastapi.tiangolo.com/) web framework.

[Uvicorn](https://www.uvicorn.org/) ASGI web server.

[Swagger UI](https://github.com/swagger-api/swagger-ui) for documentation. Swagger UI is included with fastAPI. API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

[SQLAlchemy](https://www.sqlalchemy.org/) ORM.

### Run with Docker

`docker compose up --build`

This command will run `sql_app.main:app`. `Dockerfile` can be edited to run `main:app` instead.

### Or install locally

_All instructions are for Linux._

Using [uv](https://github.com/astral-sh/uv) as Python package installer.

Install uv:

`curl -LsSf https://astral.sh/uv/install.sh | sh`

Create a virtual environment:

`uv venv`

Activate the virtual environment:

`source .venv/bin/activate`

Install from requirements:

`uv pip install -r requirements.txt`

### Run the server:

`uvicorn main:app --reload`

or for the CRUD app:

`uvicorn sql_app.main:app --reload`

API is accessible on:

`http://127.0.0.1:8000/`

### Run tests

`pytest`

### Generate requirements

`uv pip freeze > requirements.txt`

### Install and initiate Alembic for database migrations

`uv pip install alembic`

This needs to be done only once:

`alembic init alembic`

### Create a migration script

Each time the models are updated, a new revision can be created with:

`alembic revision --autogenerate -m "Added is_staff to User"`

### Upgrade the database

`alembic upgrade head`

### Downgrade the database

`alembic downgrade -1`

`-1`: Downgrades the database by one revision.

`-2`: Downgrades the database by two revisions and etc.

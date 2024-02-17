# fastapi-swagger-exploration

### Tech stack

[uv](https://github.com/astral-sh/uv) Python package installer. Reading: [uv: Python packaging in Rust](https://astral.sh/blog/uv).

[fastAPI](https://fastapi.tiangolo.com/) web framework.

[Uvicorn](https://www.uvicorn.org/) ASGI web server.

[Swagger UI](https://github.com/swagger-api/swagger-ui) for documentation. Swagger UI is included with fastAPI. API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Run with Docker

`docker compose up --build`

### Or install

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

API is accessible on:

`http://127.0.0.1:8000/`

### Run tests

`pytest`

### Generate requirements

_Note to self_.

`uv pip freeze > requirements.txt`
